# Motivation

* Infer Characteristics of the population from the sample.
* Find out confidence intervals (range of possible values) for parameters of interest

# Method

## Best Practices
- Always remember to use t-statistics for means and Z-statistics for proportions!
- A precise confidence interval has a small margin of error (ME)

## Parameter of interest
Confidence Intervals for
- p: proportions
- q: mean

# Mechanics
## Example: Proportions
Confidence Interval = C.I. = p^ +- Z@alpha/2 * se(p^)
with
- p^ = Proportion Sample
- se(p^) = Standard Error(p^) = SQRT(p(1-p)/n)
- Alpha = 0.05 (commonly used)

## Checklist

* [ ] Simple Random Sample from the relevant population
* [ ] Sample Size Condition
* [ ] n * p^ > 10
* [ ] n (1-p^) > 10

## Example: Mean
Confidence Interval = C.I. = X +- t@alpha/2|n-1 * se(X)
with

X = Mean of observed sample
se(X) = Standard Error(X) = s / Sqrt(n)
Alpha = 0.05

## Checklist

* [ ] Simple Random Sample from the relevant population
* [ ] Sample Size Condition
* [ ] n > 10|K4| (Sample Size bigger than 10 times value of kurtosis)

# Message
With 95% confidence, the population proportions that ... lies between ...
With 95% confidence, the population mean of ... lies between ...
