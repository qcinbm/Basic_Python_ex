# Basic Python Exercises

## Introduction

This repository contains basic Python exercises to evaluate classification models, implement activation functions, choose regression loss functions, approximate mathematical functions, and calculate the Mean Difference of nth Root Error (MD_nRE).

## Exercise 1: Classification Model Evaluation using F1-Score

### Description

Write a function to evaluate a classification model using F1-Score. The function should calculate Precision, Recall, and F1-Score based on true positives (tp), false positives (fp), and false negatives (fn).

### Requirements

- Ensure `tp`, `fp`, and `fn` are integers.
- Values of `tp`, `fp`, and `fn` must be greater than 0.

### Formulae
- Precision: 
  $$\text{Precision} = \frac{TP}{TP + FP}$$
- Recall: 
  $$\text{Recall} = \frac{TP}{TP + FN}$$
- F1-Score: 
  $$\text{F1-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$


### Example Usage


```python
exercise1(tp=2, fp=3, fn=4)
# Output:
>> precision is 0.4
recall is 0.3333333333333333
f1-score is 0.3636363636363636
```
## Exercise 2: Activation Functions

### Description

Write a function to simulate the following activation functions:
- Sigmoid
- ReLU
- ELU

### Requirements

- Check if `x` is a number using the provided `is_number` function.
- Validate the activation function name.
- Convert `x` to float and compute the result using the corresponding formula.

### Formulae

- Sigmoid:
  $$\text{Sigmoid}(x) = \frac{1}{1 + e^{-x}}$$
- ReLU:
  $$\text{ReLU}(x) = \max(0, x)$$
- ELU:
 $$\text{ELU}(x) = 
\begin{cases} 
x & \text{if } x > 0 \\
\alpha (e^x - 1) & \text{if } x \leq 0 
\end{cases}$$
### Example Usage

```python
exercise2()
# Example Inputs and Outputs:
# Input x = 1.5
# Input activation function (sigmoid|relu|elu): sigmoid
# Output: sigmoid: f(1.5) = 0.8175744761936437
```

## Exercise 3: Regression Loss Function

### Description

Write a function to choose and calculate a regression loss function: MAE, MSE, or RMSE.

### Requirements

- Validate `num_samples` as an integer.
- Generate random `predict` and `target` values.
- Compute the loss using the chosen function.

### Formulae

- Mean Absolute Error (MAE):
  $$\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$

- Mean Squared Error (MSE):
  $$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

- Root Mean Squared Error (RMSE):
  $$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$$

### Example Usage

```python

exercise3()
# Example Inputs and Outputs:
# Input number of samples (integer number): 5
# Input loss name: RMSE
# Output:
# RMSE: 2.345678912345678
```

## Exercise 4: Approximating Mathematical Functions

### Description

Write functions to approximate the following functions using a Taylor series expansion:
- \(\sin(x)\)
- \(\cos(x)\)
- \(\sinh(x)\)
- \(\cosh(x)\)

### Requirements

- Validate `x` as a radian and `n` as a positive integer.
- Implement a factorial function for calculations.

### Formulae

- Taylor series for \(\sin(x)\):
  $$\sin(x) \approx \sum_{k=0}^{n} \frac{(-1)^k x^{2k+1}}{(2k+1)!}$$

- Taylor series for \(\cos(x)\):
  $$\cos(x) \approx \sum_{k=0}^{n} \frac{(-1)^k x^{2k}}{(2k)!}$$

- Taylor series for \(\sinh(x)\):
  $$\sinh(x) \approx \sum_{k=0}^{n} \frac{x^{2k+1}}{(2k+1)!}$$

- Taylor series for \(\cosh(x)\):
  $$\cosh(x) \approx \sum_{k=0}^{n} \frac{x^{2k}}{(2k)!}$$

### Example Usage

```python

# Example usage:
x = 3.14
n = 10

print(f"sin({x}) ≈ {taylor_sin(x, n)}")
print(f"cos({x}) ≈ {taylor_cos(x, n)}")
print(f"sinh({x}) ≈ {taylor_sinh(x, n)}")
print(f"cosh({x}) ≈ {taylor_cosh(x, n)}")
>>sin(3.14) ≈ 0.0015926529164868282
cos(3.14) ≈ -0.999999980795569
sinh(3.14) ≈ 11.02446891315649
cosh(3.14) ≈ 11.02317637992195

```
## Exercise 5: Regression Metrics

### Description

Write a function to compute and display the following regression metrics:
- R2 Score
- Adjusted R2 Score
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

### Requirements

- Validate `y_true` and `y_pred` as lists or arrays of equal length.
- Validate `num_features` as a positive integer.
- Compute the metrics using the provided formulas.

### Formulae

- R2 Score:
  $$R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}$$

- Adjusted R2 Score:
  $$\text{Adjusted } R^2 = 1 - \left( \frac{1 - R^2}{n - k - 1} \right) (n - 1)$$
  where \( n \) is the number of observations and \( k \) is the number of features.

- Mean Squared Error (MSE):
  $$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

- Root Mean Squared Error (RMSE):
  $$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$$

### Example Usage

```python

# Example usage:
y_true = [3.0, -0.5, 2.0, 7.0]
y_pred = [2.5, 0.0, 2.1, 7.8]
num_features = 2

exercise5(y_true, y_pred, num_features)
# Example Outputs:
# R2 Score: 0.9486081370449679
# Adjusted R2 Score: 0.8958245484575467
# MSE: 0.185
# RMSE: 0.4301162633521313
```



