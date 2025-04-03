# Linear Regression

## Overview
Linear Regression is a fundamental supervised learning algorithm used for predicting continuous values. It models the relationship between an independent variable (X) and a dependent variable (Y) by fitting a straight line.

## Key Concepts

### 1. Equation of Linear Regression
Linear Regression follows the equation:

y = mx + b

Where:
- **y** = Predicted value (dependent variable)
- **m** = Slope of the line (coefficient)
- **x** = Input feature (independent variable)
- **b** = Intercept (bias term)

For multiple features (Multiple Linear Regression), the equation extends to:

y = b0 + b1x1 + b2x2 + ... + bnxn

### 2. Types of Linear Regression
- **Simple Linear Regression**: Involves one independent variable.
- **Multiple Linear Regression**: Involves multiple independent variables.
- **Polynomial Regression**: Extends linear regression by including polynomial terms for capturing non-linearity.

### 3. Assumptions of Linear Regression
Linear Regression works best under the following assumptions:
- **Linearity**: The relationship between independent and dependent variables is linear.
- **Independence**: Observations are independent of each other.
- **Homoscedasticity**: Constant variance of residuals.
- **No Multicollinearity**: Independent variables should not be highly correlated.
- **Normality of Residuals**: The residuals should be normally distributed.

### 4. Evaluation Metrics
To measure the performance of a Linear Regression model, the following metrics are used:
- **Mean Squared Error (MSE)**: Measures the average squared differences between actual and predicted values.
- **Root Mean Squared Error (RMSE)**: Square root of MSE, providing error in actual units.
- **Mean Absolute Error (MAE)**: Average absolute differences between actual and predicted values.
- **R-squared (R² Score)**: Indicates how well the independent variables explain the variance in the dependent variable.



