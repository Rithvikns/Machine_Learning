# Machine Learning: Understanding Key Parameters

Machine learning (ML) is a branch of artificial intelligence that enables computers to learn patterns from data and make predictions. When implementing ML models, various parameters and metrics are used to optimize performance and evaluate accuracy. Below are some key terms commonly encountered in ML code.

## 1. Epoch
An **epoch** represents one complete pass through the entire training dataset. During each epoch, the model updates its parameters based on the computed errors. More epochs usually improve learning but may also lead to overfitting.

## 2. Optimizer
Optimizers are algorithms used to update the model's parameters (weights and biases) to minimize loss. Common optimizers include:
- **SGD (Stochastic Gradient Descent)**: Updates parameters using a small subset (batch) of data.
- **Adam (Adaptive Moment Estimation)**: Adjusts learning rates individually for different parameters.
- **RMSprop (Root Mean Square Propagation)**: Adapts learning rates based on recent gradient magnitudes.

## 3. Loss Function
A **loss function** measures the difference between the predicted output and the actual target values. Lower loss values indicate better performance. Some common loss functions are:
- **Mean Squared Error (MSE)**: Measures the average squared differences between predicted and actual values.
- **Cross-Entropy Loss**: Used for classification tasks to compare predicted probabilities with actual labels.

## 4. Regularization: L1 and L2
Regularization techniques help prevent overfitting by adding penalties to model complexity:
- **L1 Regularization (Lasso Regression)**: Adds an absolute value penalty to the loss function, encouraging sparsity (zero weights for some features).
- **L2 Regularization (Ridge Regression)**: Adds a squared penalty, reducing large weights but not eliminating them.

## 5. Precision, Recall, and F1-Score
These metrics evaluate classification models:
- **Precision**: Measures the accuracy of positive predictions.
  \[ Precision = \frac{True Positives}{True Positives + False Positives} \]
- **Recall**: Measures the ability to find all relevant instances.
  \[ Recall = \frac{True Positives}{True Positives + False Negatives} \]
- **F1-Score**: A harmonic mean of precision and recall.
  \[ F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall} \]

## 6. Variance Score
Variance score measures how well a model captures the variability in the dataset. It is computed as:
\[ Variance Score = 1 - \frac{Variance of Errors}{Variance of Actual Values} \]
A high variance score (close to 1) indicates a good model, while a low score suggests poor generalization.

## Conclusion
Understanding these parameters is crucial for developing efficient machine learning models. Fine-tuning them can significantly impact model accuracy, training stability, and generalization to unseen data.

---
### 🔗 More Resources
- [Scikit-Learn Documentation](https://scikit-learn.org/)
- [TensorFlow Guide](https://www.tensorflow.org/)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)

