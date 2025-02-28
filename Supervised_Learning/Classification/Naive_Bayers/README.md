# Naïve Bayes Algorithm

## Introduction
Naïve Bayes is a **probabilistic classification algorithm** based on **Bayes' Theorem**. It assumes that the features are **independent** of each other, which is a strong ("naïve") assumption but often works well in practice.

## Bayes' Theorem
Bayes' Theorem states:

\[
P(A \mid B) = \frac{P(B \mid A) P(A)}{P(B)}
\]

Where:
- \( P(A \mid B) \) is the **posterior probability** (probability of A given B).
- \( P(B \mid A) \) is the **likelihood** (probability of B given A).
- \( P(A) \) is the **prior probability** of A.
- \( P(B) \) is the **marginal probability** of B.

## Types of Naïve Bayes Classifiers
1. **Gaussian Naïve Bayes (GNB)**: Assumes continuous features follow a normal distribution.
2. **Multinomial Naïve Bayes (MNB)**: Used for text classification, works well with word counts.
3. **Bernoulli Naïve Bayes (BNB)**: Suitable for binary/boolean features.
4. **Complement Naïve Bayes (CNB)**: A variation of MNB that works better for imbalanced text data.

## Advantages
✅ **Simple and fast**: Works well with large datasets and requires little training time.  
✅ **Works well with small datasets**: Even with limited data, it provides good results.  
✅ **Handles categorical & text data well**: Especially useful in spam detection, sentiment analysis, and document classification.  
✅ **Performs well with high-dimensional data**: Effective in applications like Natural Language Processing (NLP).  

## Disadvantages
❌ **Strong independence assumption**: Often unrealistic, as features are usually correlated.  
❌ **Poor estimation of probabilities with small datasets**: If a category is missing from training, it assigns zero probability (handled with **Laplace Smoothing**).  
❌ **Not ideal for continuous features**: Works best with discrete data; Gaussian Naïve Bayes tries to handle continuous data but isn't always accurate.  

## Applications of Naïve Bayes
- **Spam detection** (Email filtering)
- **Sentiment analysis** (Positive/negative reviews)
- **Medical diagnosis** (Disease prediction)
- **Credit scoring** (Risk analysis)
- **Text classification** (News categorization, language detection)

## Example Implementation in Python
```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Example dataset
X = np.array([[1, 20], [2, 21], [3, 22], [4, 23], [5, 24]])
y = np.array([0, 0, 1, 1, 1])

# Splitting data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Naïve Bayes classifier
nb = GaussianNB()
nb.fit(X_train, y_train)

# Predictions
y_pred = nb.predict(X_test)

# Accuracy
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
```

## Conclusion
Naïve Bayes is a simple yet powerful classification algorithm, particularly useful for text classification and spam filtering. However, its independence assumption can be a limitation in some cases.



