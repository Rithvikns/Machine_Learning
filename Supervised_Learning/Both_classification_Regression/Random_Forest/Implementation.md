# Random Forest - Google Colab Project

This repository demonstrates an advanced use of the Random Forest algorithm for both **classification** and **regression** using Python in Google Colab.

We'll explore hyperparameter tuning, feature importance, evaluation metrics, and visualization. 🚀

---

## 📊 Dataset Information

### 1. **Wine Dataset (for Classification)**
- Source: Scikit-learn built-in dataset
- Description: Contains chemical analysis results of wines grown in the same region in Italy but derived from three different cultivars.
- Features:
  - Alcohol
  - Malic acid
  - Ash
  - Alcalinity of ash
  - Magnesium
  - Total phenols
  - Flavanoids
  - Nonflavanoid phenols
  - Proanthocyanins
  - Color intensity
  - Hue
  - OD280/OD315 of diluted wines
  - Proline
- Target: Wine class (0, 1, 2)

### 2. **Synthetic Regression Dataset (for Regression Task)**
- Generated using `make_regression()` from Scikit-learn.
- 500 samples, 5 features, with added noise.

---

## 📦 Code Breakdown

### 📥 Installation & Import
We start by installing and importing all necessary libraries like `scikit-learn`, `matplotlib`, and `seaborn` for machine learning and visualization.

### 🧩 Data Loading & Visualization
We load the Wine dataset and visualize class distribution using Seaborn's `countplot()` to understand class imbalance.

```python
sns.countplot(x=y, palette='viridis')
```

### ✂️ Data Splitting
Split the dataset into training and testing sets using `train_test_split()`.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

### 🌲 Model Training: Random Forest Classifier
We initialize the Random Forest Classifier and tune hyperparameters using **GridSearchCV** to find the optimal combination.

```python
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'max_features': ['sqrt', 'log2']
}

grid_search = GridSearchCV(clf, param_grid, cv=3, scoring='accuracy', verbose=1, n_jobs=-1)
grid_search.fit(X_train, y_train)
```

### 🧮 Evaluation Metrics
We evaluate model performance using:
- **Classification report** (precision, recall, F1-score)
- **Confusion matrix heatmap**
- **Accuracy score**

```python
print(classification_report(y_test, y_pred))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True)
```

### 🔍 Feature Importance
Visualize which features are most important to the model using a bar plot.

```python
sns.barplot(x=importances[indices], y=features[indices], palette='rocket')
```

### 📈 Regression Task (Bonus!)
To demonstrate versatility, we also apply Random Forest to a synthetic regression problem, evaluating with **Mean Squared Error (MSE)** and a scatter plot of actual vs predicted values.

```python
reg = RandomForestRegressor(n_estimators=100, random_state=42)
reg.fit(X_reg_train, y_reg_train)
print(mean_squared_error(y_reg_test, y_reg_pred))
```

---

## 🎨 Visual Outputs
- ✅ Class distribution plot
- ✅ Confusion matrix heatmap
- ✅ Feature importance bar chart
- ✅ Regression actual vs predicted scatter plot

---

## 🚀 How to Run
1. Open the notebook in Google Colab.
2. Install required libraries (most are pre-installed in Colab).
3. Run each cell step by step.
4. Observe outputs and visualizations!

---

## 🤖 Technologies Used
- Python 3
- Scikit-learn
- Matplotlib
- Seaborn
- NumPy / Pandas

---


## 💡 Future Enhancements
- Add cross-validation visualization
- Export model using `joblib`
- Visualize individual trees in the forest
- Compare Random Forest with other algorithms like XGBoost or SVM

---

Enjoy learning Random Forest! 🌲✨

---

