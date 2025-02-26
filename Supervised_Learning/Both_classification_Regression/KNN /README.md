# KNN (K - Nearest Neighbours)

It is one of the most simplest and most intuitive algorithm used in machine learning for classification and regression task.
KNN is a non parametric lazy learning algorithm .

### Lazy Learning 

It doesn't compute the discriminating function during the training phase but instead it memorises the training data and computes during the prediction phase. Hence the name lazy learner

KNN works by comparing the new input data points with the data points in the training dataset that are closest in feature space.

KNN Working

1) Choose the number k , i.e k is the number of nearest neighbours to consider.
2) calculate the distance using methods such as

   
   Euclidean Distance


   manhattan distance


   Minkowski distance : generalisation form which includes both euclidean and manhattan distance as special cases


   Hamming distance.
4) Sort the distances.
5) pick the nearest neighbours.
6) Vote for classification task , Average for regression task.


## Advantages of KNN

Simple and intuitive


No training period


Adaptable to new data

## Disadvantages of KNN

Computationally expensive (comparing the input point with all other points in the dataset)


Slow


Memory intensive


sensitivity to irrelevant features


choice of K


not scalable.

## Dataset

### 🍷 Wine Quality Prediction using K-Nearest Neighbors (KNN)

This project applies the **K-Nearest Neighbors (KNN) algorithm** to predict wine quality based on **physicochemical properties**.

---

### 📂 Dataset: Wine Quality
The dataset consists of **13 numerical features** that describe different chemical properties of wine. The goal is to classify wines into **three quality categories**.

### **Features (X)**
| Feature                  | Description                                        |
|--------------------------|----------------------------------------------------|
| **Alcohol**              | Alcohol content (%)                                |
| **Malic Acid**           | Type of acid present in wine                      |
| **Ash**                  | Residue left after burning the wine sample        |
| **Alcalinity of Ash**    | pH level of the ash                               |
| **Magnesium**            | Magnesium content (mg/L)                          |
| **Total Phenols**        | Antioxidants present in the wine                  |
| **Flavanoids**           | Type of phenolic compound (affects taste)         |
| **Nonflavanoid Phenols** | Other phenols in the wine                         |
| **Proanthocyanins**      | Tannins that influence color and bitterness       |
| **Color Intensity**      | Depth of color in the wine                        |
| **Hue**                  | Shade of color (yellowish, reddish, etc.)         |
| **OD280/OD315**          | Ratio of absorbance of light (related to phenols) |
| **Proline**              | Amino acid that affects taste                     |

### **Target Variable (y)**
- **Class 0** → Type 1 Wine  
- **Class 1** → Type 2 Wine  
- **Class 2** → Type 3 Wine  

📌 Dataset Source:  
- **Scikit-learn Version**: `load_wine()`  
- **UCI Wine Quality Dataset**: [Download Here](https://archive.ics.uci.edu/ml/datasets/Wine+Quality)

---

### 🚀 Implementation in Google Colab
The KNN model is implemented in **Python (Scikit-learn)** and runs in **Google Colab**.

### **🔹 Steps**
1. **Load dataset** (`sklearn.datasets.load_wine()`).
2. **Split** data into **training (80%)** and **testing (20%)** sets.
3. **Standardize** features using `StandardScaler()`.
4. **Train KNN model** (`KNeighborsClassifier(n_neighbors=7)`).
5. **Evaluate** model accuracy & visualize results.


## Resources

For more details you can refer to : https://scikit-learn.org/1.6/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
