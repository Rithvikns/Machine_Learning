# Logistic Regression

## Overview
Logistic Regression is a supervised learning algorithm used for **classification tasks**. Despite its name, it is not used for regression but rather for predicting categorical outcomes. It estimates the probability of an instance belonging to a particular class using the **sigmoid (logistic) function**.

## How It Works
1. Computes a weighted sum of input features:
   ```math
   z = w_1x_1 + w_2x_2 + ... + w_nx_n + b
   ```
2. Applies the **sigmoid function** to convert `z` into a probability value:
   ```math
   \sigma(z) = \frac{1}{1 + e^{-z}}
   ```
3. Uses a decision threshold (typically 0.5) to classify the output:
   - If `σ(z) ≥ 0.5`, predict class **1**
   - If `σ(z) < 0.5`, predict class **0**

## Types of Logistic Regression
- **Binary Logistic Regression**: Classifies data into two categories (e.g., spam vs. not spam).
- **Multinomial Logistic Regression**: Handles multi-class problems where classes are not ordered.
- **Ordinal Logistic Regression**: Used for ordered categories (e.g., low, medium, high).

## Advantages
- Simple and easy to interpret.
- Works well for linearly separable data.
- Outputs probabilities, which can be useful in decision-making.

## Limitations
- Assumes a linear relationship between features and log-odds.
- Not ideal for highly complex, non-linear problems.
- Sensitive to imbalanced datasets.

## Applications
- **Medical Diagnosis**: Predicting disease presence.
- **Spam Detection**: Classifying emails as spam or not spam.
- **Customer Churn Prediction**: Identifying customers likely to leave a service.
- **Fraud Detection**: Identifying fraudulent transactions.

## Conclusion
Logistic Regression is a powerful yet simple classification algorithm. It is widely used for binary and multi-class classification tasks. Despite its limitations, it remains a fundamental algorithm in machine learning.
