# Support Vector Machine (SVM) Algorithm

## Overview
Support Vector Machine (SVM) is a supervised learning algorithm used for classification and regression tasks. It works by finding the optimal hyperplane that best separates different classes in a dataset.

## Key Concepts
### 1. Hyperplane
- A decision boundary that separates data points into different classes.
- The optimal hyperplane maximizes the **margin** between support vectors.

### 2. Support Vectors
- Data points that lie closest to the decision boundary.
- These points define the margin and influence the hyperplane's position.

### 3. Kernel Trick
- SVM can transform non-linearly separable data into a higher-dimensional space where a linear separator can be found.
- Common kernel functions:
  - **Linear Kernel**: Suitable for linearly separable data.
  - **Polynomial Kernel**: Suitable for complex relationships.
  - **Radial Basis Function (RBF) Kernel**: Used for non-linear data.
  - **Sigmoid Kernel**: Used in neural networks.

### 4. Soft Margin vs. Hard Margin
- **Hard Margin**: Strict separation; works well with linearly separable data but sensitive to noise.
- **Soft Margin**: Allows some misclassification to improve generalization.

## SVM for Classification
SVM finds the best hyperplane to separate different classes in a dataset.

### Example
```python
from sklearn.svm import SVC
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate dataset
X, y = make_classification(n_samples=100, n_features=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train SVM classifier
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
```

## SVM for Regression (SVR)
SVM can also be used for regression by fitting a function within a given margin.

### Example
```python
from sklearn.svm import SVR
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generate dataset
X, y = make_regression(n_samples=100, n_features=1, noise=0.1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train SVM regressor
model = SVR(kernel='rbf')
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, y_pred))
```

## Advantages of SVM
- Effective in high-dimensional spaces.
- Works well with small datasets.
- Robust to overfitting (especially with proper kernel selection).

## Disadvantages of SVM
- Computationally expensive for large datasets.
- Requires careful selection of kernel and hyperparameters.

## Applications of SVM
- Image classification (e.g., handwritten digit recognition)
- Text categorization (spam detection, sentiment analysis)
- Bioinformatics (protein classification)

## References
- [Scikit-learn SVM Documentation](https://scikit-learn.org/stable/modules/svm.html)
- [Wikipedia: Support Vector Machine](https://en.wikipedia.org/wiki/Support_vector_machine)

## License
This project is licensed under the MIT License.

