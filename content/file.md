Linear Regression
Overview
Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables. The goal is to find the best-fitting line through the data points.
Simple Linear Regression
Model
The simple linear regression model can be expressed as:
y = β₀ + β₁x + ε
Where:

y is the dependent variable.
x is the independent variable.
β₀ is the y-intercept.
β₁ is the slope of the line.
ε is the error term.

Estimating Coefficients
The coefficients β₀ and β₁ are estimated using the least squares method:
β₁ = (n(Σxy) - (Σx)(Σy)) / (n(Σx²) - (Σx)²)
β₀ = ȳ - β₁x̄
Where:

n is the number of data points.
Σxy is the sum of the product of x and y.
Σx is the sum of x values.
Σy is the sum of y values.
Σx² is the sum of the squares of x values.
x̄ and ȳ are the means of x and y respectively.

Prediction
To make predictions using the model, substitute x into the equation:
ŷ = β₀ + β₁x
Where ŷ is the predicted value of y.
Multiple Linear Regression
Model
The multiple linear regression model is an extension of simple linear regression, expressed as:
y = β₀ + β₁x₁ + β₂x₂ + ... + βₚxₚ + ε
Where x₁, x₂, ..., xₚ are independent variables.
Estimating Coefficients
Coefficients in multiple linear regression can be estimated using matrix notation:
β = (X^T X)^(-1) X^T y
Where:

β is the vector of coefficients.
X is the matrix of input features.
y is the vector of outputs.

Goodness of Fit
R-squared
The R-squared value indicates the proportion of the variance in the dependent variable that is predictable from the independent variables:
R² = 1 - (SS_res / SS_tot)
Where:

SS_res is the sum of squares of residuals.
SS_tot is the total sum of squares.

Adjusted R-squared
Adjusted R-squared adjusts the statistic based on the number of predictors in the model:
R̄² = 1 - (1 - R²) * ((n - 1) / (n - p - 1))
Where p is the number of predictors.
Conclusion
Linear regression is a fundamental tool in statistics and machine learning for understanding relationships between variables and making predictions. Understanding the underlying mathematics is crucial for effectively applying linear regression techniques.