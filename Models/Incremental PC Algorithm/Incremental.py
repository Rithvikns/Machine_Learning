import numpy as np
import networkx as nx
import pandas as pd
from causallearn.search.ConstraintBased.PC import pc
from causallearn.utils.cit import fisherz
from scipy.stats import ks_2samp

class IncrementalPC:
    def __init__(self, initial_data, alpha=0.05):
        """
        Initialize IPCD with an initial dataset.

        :param initial_data: Pandas DataFrame, initial dataset.
        :param alpha: Significance level for conditional independence tests.
        """
        self.alpha = alpha
        self.data = initial_data.copy()
        self.variables = list(self.data.columns)
        self.graph = self.run_pc(initial_data)  # Initial causal graph
        self.cache = {}  # Store independence test results

    def run_pc(self, data):
        """Run the standard PC algorithm on a dataset and return a NetworkX graph."""
        cg = pc(data.to_numpy(), alpha=self.alpha, indep_test=fisherz)
        adj_matrix = cg.G.graph  # Get adjacency matrix
        g = nx.from_numpy_matrix(adj_matrix, create_using=nx.DiGraph)  # Convert to NetworkX
        return g

    def detect_distribution_shift(self, new_data):
        """
        Detect significant distribution shifts between old and new data.

        :param new_data: Pandas DataFrame, new data batch.
        :return: List of changed variables.
        """
        changed_vars = []
        for col in self.variables:
            stat, p_value = ks_2samp(self.data[col], new_data[col])
            if p_value < 0.1:  # **More lenient threshold**
                changed_vars.append(col)
        return changed_vars

    def incremental_update(self, new_data):
        """
        Update the causal graph based on new data, modifying only affected edges.

        :param new_data: Pandas DataFrame, new data batch.
        """
        changed_vars = self.detect_distribution_shift(new_data)
        if not changed_vars:
            print("No significant changes detected. Skipping update.")
            return

        # Merge new data with existing dataset
        self.data = pd.concat([self.data, new_data]).tail(1000)  # Keep recent 1000 points

        # **Run PC Algorithm again on updated dataset**
        new_graph = self.run_pc(self.data)

        # **Compare and update edges for affected variables**
        for var in changed_vars:
            for neighbor in self.variables:
                if var != neighbor:
                    old_edge = self.graph.has_edge(self.variables.index(var), self.variables.index(neighbor))
                    new_edge = new_graph.has_edge(self.variables.index(var), self.variables.index(neighbor))

                    if new_edge and not old_edge:
                        print(f"Adding edge: {var} → {neighbor}")
                        self.graph.add_edge(self.variables.index(var), self.variables.index(neighbor))
                    elif old_edge and not new_edge:
                        print(f"Removing edge: {var} → {neighbor}")
                        self.graph.remove_edge(self.variables.index(var), self.variables.index(neighbor))

    def get_graph(self):
        """Return the current causal graph as an adjacency matrix."""
        return nx.to_numpy_matrix(self.graph)
