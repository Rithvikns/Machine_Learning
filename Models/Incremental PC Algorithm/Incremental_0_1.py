import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from causallearn.search.ConstraintBased.PC import pc
from causallearn.utils.cit import fisherz
from scipy.stats import ks_2samp

class IncrementalPC:
    def __init__(self, initial_data, alpha=0.05):
        self.alpha = alpha
        self.data = initial_data.copy()
        self.num_vars = initial_data.shape[1]  # Number of variables
        self.graph = self.run_pc(self.data)  # Keep as NumPy array
        self.cache = {}

    def run_pc(self, data):
        """Run the standard PC algorithm on a dataset and return a NetworkX graph."""
        cg = pc(data, alpha=self.alpha, indep_test=fisherz)
        adj_matrix = cg.G.graph
        g = nx.DiGraph()
        
        for i in range(self.num_vars):
            for j in range(self.num_vars):
                if adj_matrix[i, j]:  # If there is an edge
                    g.add_edge(i, j)
        
        return g

    def detect_distribution_shift(self, new_data):
        """Detect significant distribution shifts between old and new data."""
        changed_vars = []
        for i in range(self.num_vars):
            stat, p_value = ks_2samp(self.data[:, i], new_data[:, i])
            if p_value < 0.1:
                changed_vars.append(i)
        return changed_vars

    def incremental_update(self, new_data):
        """Update the causal graph based on new data, modifying only affected edges."""
        changed_vars = self.detect_distribution_shift(new_data)
        if not changed_vars:
            print("No significant changes detected. Skipping update.")
            return

        self.data = np.vstack((self.data, new_data))[-1000:, :]  # Keep recent 1000 points
        new_graph = self.run_pc(self.data)

        for var in changed_vars:
            for neighbor in range(self.num_vars):
                if var != neighbor:
                    old_edge = self.graph.has_edge(var, neighbor)
                    new_edge = new_graph.has_edge(var, neighbor)
                    
                    if new_edge and not old_edge:
                        print(f"Adding edge: {var} → {neighbor}")
                        self.graph.add_edge(var, neighbor)
                    elif old_edge and not new_edge:
                        print(f"Removing edge: {var} → {neighbor}")
                        self.graph.remove_edge(var, neighbor)

    def get_graph_matrix(self):
        """Return the current causal graph as an adjacency matrix."""
        return nx.to_numpy_matrix(self.graph)
    
    def display_graph(self):
        """Display the causal graph as a visual representation."""
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_size=3000, node_color='lightblue', edge_color='gray', font_size=10, font_weight='bold')
        plt.title("Causal Graph")
        plt.show()
