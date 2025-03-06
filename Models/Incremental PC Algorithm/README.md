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

# Explanation of IncrementalPC Code

## Overview
The `IncrementalPC` class is designed for **incremental causal discovery**, meaning it updates an existing causal graph when new data arrives instead of recomputing everything from scratch. It uses the **PC (Peter-Clark) algorithm** to infer causal relationships between variables in a dataset.

---
## 1. Initialization (`__init__` method)
### **Purpose:**
- Initializes the class with an initial dataset and a significance level (`alpha`).
- Runs the **PC algorithm** to generate an initial causal graph.

### **Key Actions:**
- Stores the provided dataset.
- Runs the PC algorithm to compute the initial causal structure.
- Converts the adjacency matrix into a **NetworkX graph** for easier manipulation.

---
## 2. Running the PC Algorithm (`run_pc` method)
### **Purpose:**
- Runs the **PC algorithm** from the `causallearn` library to infer causal relationships.

### **Key Actions:**
- Converts the dataset into a **NumPy array**.
- Applies the **PC algorithm**, which identifies conditional independence relationships.
- Generates a **graph representation** of the causal structure using NetworkX.

**Note:** The `verbose=False` parameter suppresses progress bars in the output.

---
## 3. Detecting Distribution Shifts (`detect_distribution_shift` method)
### **Purpose:**
- Determines whether the new data is significantly different from the old data.
- Uses the **Kolmogorov-Smirnov (KS) test**, a statistical test that compares two distributions.

### **Key Actions:**
- Iterates through each column (variable) in the dataset.
- Computes the KS test statistic and p-value.
- If the **p-value is below 0.05**, the variable is considered to have undergone a significant shift.

---
## 4. Incremental Update (`incremental_update` method)
### **Purpose:**
- Updates the causal graph only if significant changes in data distribution are detected.

### **Key Actions:**
1. **Detect Changes**: Runs `detect_distribution_shift()` to check if any variables have changed significantly.
2. **Merge Data**: If changes are detected, merges the new data with the existing dataset (keeping only the most recent 1000 rows).
3. **Update Graph**: Recomputes the causal structure using `run_pc()`.

### **Edge Updates:**
- If a **new dependency is found**, an edge is added.
- If a **previous dependency is no longer valid**, an edge is removed.

---
## 5. Retrieving the Final Graph (`get_graph` method)
### **Purpose:**
- Returns the current causal graph as an **adjacency matrix**.
- Can be used for visualization or further analysis.

---
## **Summary of Workflow**
1. **Initialize** the class with an initial dataset.
2. **Run the PC Algorithm** to determine the initial causal relationships.
3. **When new data arrives**, check if there are significant changes in the dataset.
4. **If significant changes are detected**, update the causal graph.
5. **Retrieve the final causal structure** as an adjacency matrix.

This approach allows **efficient real-time updates** without needing to recompute the entire causal graph from scratch, making it suitable for streaming or dynamically changing datasets.



## Expected Output
During execution, the script should output messages indicating when edges are added or removed from the causal graph. The final causal graph is displayed as an adjacency matrix.
```console
Depth=0, working on node 2: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<?, ?it/s]

---- Update 1 ----
Depth=0, working on node 2: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<?, ?it/s]

---- Update 2 ----
Depth=0, working on node 2: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 273.00it/s]

---- Update 3 ----
Depth=0, working on node 2: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 312.34it/s]

---- Update 4 ----
Depth=0, working on node 2: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<?, ?it/s] 
Adding edge: A → B
Adding edge: B → A

---- Update 5 ----
Depth=0, working on node 2: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 653.18it/s] 

Final Causal Graph (Adjacency Matrix):
[[0. 1. 0.]
 [1. 0. 0.]
 [0. 0. 0.]]
```

## License
This project is open-source and available for modification and distribution.

## Contributors
- **Your Name** Rithvik Narayana Swamy

---

This `README.md` file explains the functionality, installation, and usage of `IncrementalPC`. It is structured in a **GitHub-friendly** format, making it easy for users to understand and implement. 🚀


