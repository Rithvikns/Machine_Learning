import glob
import os
import numpy as np
import pandas as pd
import time
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from causallearn.search.ConstraintBased.PC import pc
from Incremental import IncrementalPC

def z_score_normalization(df):
    return (df - df.mean()) / df.std()

def get_excel_files(directory):
    file_list = glob.glob(os.path.join(directory, "*_samples.xlsx"))
    file_list = [f for f in file_list if os.path.basename(f).split('_')[0].isdigit()]
    return sorted(file_list, key=lambda x: int(os.path.basename(x).split('_')[0]), reverse=True)

def load_sheets(file_list, num_sheets=6):
    dataframes = {}
    for file in file_list:
        sheets = pd.read_excel(file, sheet_name=None)
        sheet_names = list(sheets.keys())[:num_sheets]
        dataframes[file] = {name: sheets[name] for name in sheet_names}
    return dataframes

def update_causal_graph(df_result, incremental_model):
    df_result.loc[:, df_result.columns[1:]] = z_score_normalization(df_result.iloc[:, 1:])
    print("\nUpdated Data with Normalization:\n", df_result)
    
    data_array = df_result.to_numpy()
    if incremental_model is None:
        incremental_model = IncrementalPC(data_array, alpha=0.05)
    else:
        incremental_model.incremental_update(data_array)
    
    print("\nFinal Causal Graph (Adjacency Matrix):")
    incremental_model.display_graph()
    
    return incremental_model

def process_data(dataframes):
    timestamp = 0
    data_history = []
    incremental_model = None  # Initialize IncrementalPC instance as None
    
    for file, sheets in dataframes.items():
        min_cols = min(len(df.columns) for df in sheets.values())
        
        for col_idx in range(min_cols):
            timestamp += 2
            row_data = {"Time": timestamp}

            for sheet_name, df in sheets.items():
                column_name = df.columns[col_idx]
                column_data = df[column_name]

                for i in range(6):
                    row_data[f"car_{i+1}_{sheet_name}"] = column_data[i]
                for i in range(3):
                    row_data[f"charger_{i+1}_{sheet_name}"] = column_data[i+6]

            data_history.append(row_data)
            print(timestamp)
            if len(data_history) == 55:
                df_result = pd.DataFrame(data_history)
                incremental_model = update_causal_graph(df_result, incremental_model)

            time.sleep(0.05)

def main():
    directory = "C:/Users/rithv/Desktop/npz/"  # Adjust as needed
    file_list = get_excel_files(directory)
    dataframes = load_sheets(file_list)
    process_data(dataframes)

if __name__ == "__main__":
    main()
