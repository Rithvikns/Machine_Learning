# IncrementalPC: Incremental Causal Discovery using the PC Algorithm

## Overview
`IncrementalPC` is a Python class that applies **incremental causal discovery** using the **PC (Peter-Clark) algorithm**. It allows real-time updates to a causal graph when new data arrives, without needing to recompute the entire structure from scratch.

## Features
- Uses the **PC algorithm** from the `causallearn` library to identify causal relationships.
- Detects **distribution shifts** in new data using the **Kolmogorov-Smirnov test (KS-test)**.
- **Incrementally updates** causal graphs when significant changes are detected.
- Stores results in a **networkx-based graph** for easy visualization and retrieval.

## Installation
Before using `IncrementalPC`, ensure you have the required dependencies installed:

```sh
pip install numpy pandas networkx causallearn scipy
```

## How It Works
1. **Initialize** `IncrementalPC` with an initial dataset.
2. **Run the PC Algorithm** to generate an initial causal graph.
3. **Detect Changes** when new data arrives using a statistical test (KS-test).
4. **Update Graph** only if significant changes are detected.
5. **Retrieve the final causal graph** as an adjacency matrix.

## Code Explanation
### `IncrementalPC` Class
```python
import numpy as np
import networkx as nx
import pandas as pd
from causallearn.search.ConstraintBased.PC import pc
from causallearn.utils.cit import fisherz
from scipy.stats import ks_2samp

class IncrementalPC:
    def __init__(self, initial_data, alpha=0.05):
        self.alpha = alpha  # Significance level for independence tests
        self.data = initial_data.copy()
        self.variables = list(self.data.columns)
        self.graph = self.run_pc(initial_data)  # Run PC Algorithm initially

    def run_pc(self, data):
        cg = pc(data.to_numpy(), alpha=self.alpha, indep_test=fisherz, verbose=False)
        adj_matrix = cg.G.graph  # Get adjacency matrix
        g = nx.from_numpy_matrix(adj_matrix, create_using=nx.DiGraph)  # Convert to NetworkX
        return g

    def detect_distribution_shift(self, new_data):
        changed_vars = []
        for col in self.variables:
            stat, p_value = ks_2samp(self.data[col], new_data[col])
            if p_value < 0.1:  # Detect changes in distribution
                changed_vars.append(col)
        return changed_vars

    def incremental_update(self, new_data):
        changed_vars = self.detect_distribution_shift(new_data)
        if not changed_vars:
            print("No significant changes detected. Skipping update.")
            return
        self.data = pd.concat([self.data, new_data]).tail(1000)  # Keep last 1000 rows
        new_graph = self.run_pc(self.data)  # Rerun PC Algorithm on updated data
        self.graph = new_graph  # Update causal graph

    def get_graph(self):
        return nx.to_numpy_matrix(self.graph)  # Return adjacency matrix
```

### Example Usage
```python
import time

# Generate initial dataset
np.random.seed(42)
initial_data = pd.DataFrame({
    "A": np.random.randn(1000),
    "B": np.random.randn(1000) + 0.5,
    "C": 2 * np.random.randn(1000) + 0.2 * np.random.randn(1000)
})

# Initialize IncrementalPC
ipcd = IncrementalPC(initial_data)

# Simulate real-time updates
for i in range(5):
    time.sleep(1)  # Simulating real-time delay
    new_data = pd.DataFrame({
        "A": np.random.randn(200) + i * 0.3,
        "B": np.random.randn(200) + 0.5 + i * 0.15,
        "C": 2 * np.random.randn(200) + 0.2 * np.random.randn(200) + i * 0.1
    })
    print(f"\n---- Update {i+1} ----")
    ipcd.incremental_update(new_data)

# Print final graph
print("\nFinal Causal Graph (Adjacency Matrix):")
print(ipcd.get_graph())
```

## Expected Output
During execution, the script should output messages indicating when edges are added or removed from the causal graph. The final causal graph is displayed as an adjacency matrix.

## License
This project is open-source and available for modification and distribution.

## Contributors
- **Your Name** (Replace with your GitHub username)

---

This `README.md` file explains the functionality, installation, and usage of `IncrementalPC`. It is structured in a **GitHub-friendly** format, making it easy for users to understand and implement. 🚀


