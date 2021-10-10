# Statistics Questions & Answers

### 1. Can you explain the Central Limit Theorem (CLT)?

(General data science > Statistics)

##### Answer:
For a population with any distribution, the Sampling distribution of sample means approaches 
a Normal distribution as the sample size increases.

If you need further explanation, a sampling distribution is a probability distribution of 
a statistic obtained through a large number of samples drawn from a specific population.

The CLT is important because the normal distribution is used to help measure the accuracy 
of many statistics, including the sample mean. Thanks to the CLT is possible to measure how much the 
means of various samples will vary, without having to take any other sample means to compare it with. 
By taking this variability into account, you can use your data to answer questions about a population, 
and perform hypothesis tests and stablish confidence intervals.


### 2. What measures do you know to characterise a distribution?

(General data science > Statistics)

##### Answer:
There are mainly three types of measures:
- **Central Tendency**
- **Variation**
- **Shape**

Within these types we have:
- Central Tendency
    - Mean
    - Median
    - Mode

- Variation
    - Variance
    - Standard Deviation
    - Inter-Quantile Range

- Shape
    - Skewness
    - Kustosis

Some concepts:

When applying imputation for missing values, the mean is typically used, unless there are outliers
in which case is better to apply the median which is robust to outliers.

If a variable is skewed, 'Log transformation' can be helpful to make it more symmetric.
- Right skewed distribution => mean > median > mode
- Left skewed distribution => mean < median < mode

Is different calculating metrics for samples vs populations. For example in the variance, for population
variance the denominator is '*n*' while for sample variance is '*n-1*'.


### 3. What are the assumptions of Linear Regression?

(General data science > Statistics)

##### Answer:
1. Linearity: There is a linear relationship between dependent and independent variable. 
This is crucial as if there is non-linear relationship among dependent and independent variables, 
Linear regression model will be under-fitted and predictions will be quite far from the solution.
2. Normality: Residuals error are assumed to be normally distributed. 
Let’s see what does it mean with example: 1. See the following graph, We are trying to analyze the relationship 
between number of bids(X) requested by construction contractors and time (Y) required to prepare the bids.
3. Homoscedasticity: Residuals(Errors) are assumed to have constant variance across the level of X.


### 4. Relation between Correlation and Covariance

(General data science > Statistics)

##### Answer:
Both determine the relationship and dependency between two variables. But correlation is standardised 
between -1 and 1 while covariance is not.


### 5. Explain the p-value

(General data science > Statistics)

##### Answer:
The short answer is that the p-value reflects the strength of evidence against the null hypothesis.

Given that the null hypothesis is true (whatever premise we have) p-value is the probability of observing 
the premise in a sample from the population, and if the probability is too small, we reject the null 
hypothesis, otherwise we accept it saying that we do not have enough statistical evidence to reject it.

- p-value > 0.05 denotes weak evidence against the null hypothesis which means the null hypothesis cannot be rejected.
- p-value < 0.05 denotes strong evidence against the null hypothesis which means the null hypothesis can be rejected.
- p-value = 0.05 is the marginal value indicating it is possible to go either way.


### 6. How can you calculate a Confidence Interval?

(General data science > Statistics)

##### Answer:
A confidence interval helps us to measure and understand the uncertainty on any particular statistic.
For example, how confident we are that the sample reflects the parameters of the entire population.
The confidence level specifies how frequently the confidence interval contains the parameter. 95% is a 
commonly used confidence level which means that in repeated sampling 95% of the confidence intervals include the parameter. 

To find the confidence interval you can use the normal distribution, but as you will typically work 
with samples (<30), you will use the t-distribution.

For example for the conf internal of the mean:

1. Find the t-value, using alpha (for 95%, we enter 0.025) and the degrees of freedom (n-1) for 10 samples then 9
2. Calculate St Error = St Dev / n^(1/2)
3. Multiply t-value and the St. Error for the mean and sum/subtract to the mean.
   
[More info](https://www.statisticshowto.com/probability-and-statistics/confidence-interval/)


### 7. Difference between factor analysis and principal Component Analysis

(General data science > Statistics)

##### Answer:
Both can be used to reduce the dimensions in the data.

Factor analysis seeks linear combinations of variables (factors) that represent underlying fundamental 
quantities of which the observed variables are expressions. The variables are linear combinations 
of the factors, plus unique (or specific) factors.

PCA on the other hand summarizes common variation in many variables using just a few variables. 
To sum, reducing the number of variables of a data set, while preserving as much information as possible.

1. Standardize the range of continuous initial variables
2. Compute the covariance matrix to identify correlations
3. Compute the eigenvectors and eigenvalues of the covariance matrix to identify the principal components
4. Create a feature vector to decide which principal components to keep
5. Recast the data along the principal components axes

[More info](https://builtin.com/data-science/step-step-explanation-principal-component-analysis)
