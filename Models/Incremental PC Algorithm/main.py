import time
import numpy as np
import pandas as pd
from Incremental import IncrementalPC

# **Generate initial dataset with slight dependencies**
np.random.seed(42)
initial_data = pd.DataFrame({
    "A": np.random.randn(1000),
    "B": np.random.randn(1000) + 0.5,
    "C": 2 * np.random.randn(1000) + 0.2 * np.random.randn(1000)
})

# **Initialize IPCD**
ipcd = IncrementalPC(initial_data)

# **Simulate new data arriving over time**
for i in range(5):  # Simulate 5 update cycles
    time.sleep(1)  # Simulate delay

    # **Introduce gradual mean shifts and dependency**
    shift = i * 0.3  # Increase shift over time
    new_data = pd.DataFrame({
        "A": np.random.randn(200) + shift,  
        "B": np.random.randn(200) + 0.5 + shift / 2,  
        "C": 2 * np.random.randn(200) + 0.2 * np.random.randn(200) + shift / 3  
    })

    print(f"\n---- Update {i+1} ----")
    ipcd.incremental_update(new_data)

# **Final causal graph**
print("\nFinal Causal Graph (Adjacency Matrix):")
print(ipcd.get_graph())
