# Think Stats by Allen B. Downey

[Think Stats, 2nd Edition](http://greenteapress.com/thinkstats2/index.html)

"This book is an introduction to the practical tools of exploratory data analysis," and uses a computational and project-based approach.

"If you have never studied statistics, I think this book is a good place to start. And if you have taken a traditional statistics class, I hope this book will help repair the damage."




## Chapter 2

### distribution

  - the values that appear in the sample and the frequency of each

  - frequency: the number of times a value appears in the sample

  - normal distribution: idealized bell-shape aka Gaussian distribution

  - uniform distribution: all values have the same frequency

  - can be observed with a histogram

### summarizing distribution

  - central tendency

    - do the values tend to cluster around a particular point?

    - measured by mean

  - modes

    - what is the most frequent value?

    - is there more than one cluster?

  - spread

    - how much variability is there in the values?

    - measured by variance

    - the square root of variance is the standard deviation

  - tails

    - how quickly do probabilities drop off as we move away from the modes?

  - outliers

    - are there extreme values far from the modes?

## Chapter 3

### probability

  - probability = frequency / sample size

  - normalization: the process of dividing frequency by sample size to get probability

    - results are normalized when all probabilities add up to 1

  - probability mass function (PMF)

    - a representation of a distribution as a function that maps from values to probabilities

    - advantageous over histogram when comparing two distributions because not mislead by the sample size

### pandas

  - df = pd.DataFrame(array, index=['a', 'b', 'c', 'd'], columns=['A', 'B'])

    - index == rows

  - simple indexing selects a column and returns series

    - df['A']

  - loc selects row by label

    - df.loc['a'] returns series

    - df.loc['a', 'b'] returns dataframe

  - iloc selects row by integer index and returns series

    - df.iloc[0]

  - slice to select a range of rows

    - df['a':'c']

    - df[0:2]

## Chapter 4

### limits of PMFs

  - hard to compare visually

  - as the number of values increases

    - the probability associated with each value gets smaller

    - the effect of random noise increases

  - these problems can be mitigated with binning the data

    - dividing the range of values into non-overlapping intervals

    - counting the number of values in each bin

  - can be tricky getting the size of the bins right

    - they can smooth out noise if there are enough in the bin

    - but they can also smooth out useful info

### percentiles

  - test score example

    - fraction of the people who scored lower than you (or the same)

    - in the 90th percentile = you did as well or better than 90% of the test takers

  - percentile = the value associated with a given percentile rank

  - percentile rank = the percentage of values in a distribution that are less than
  or equal to a given value


### cumulative distribution function (CDF)

  - CDF = function that maps from a value to its percentile rank

    - CDF(x)

      - x is any value within the distribution

      - doesn't necessarily have to be in the sample

        - if x is less than the smallest value in the sample, CDF(x) = 0

        - if x is greater than the largest value in the sample, CDF(x) = 1

      - to evaluate, compute the fraction of values in the distribution less than
      or equal to x

  - Cdf.PercentileRank(x)

    - compute percentile rank of x

    - 100 * CDF(x)

  - Cdf.Percentile(p)

    - given percentile rank p, compute value of x

    - Value(p/100)

### percentile-based summary statistics

  - median

    - 50th percentile that divides the distribution in half

    - measure of the central tendency of the distribution

  - interquartile range (IQR)

    - difference between the 75th and 25th percentiles

    - measure of the spread of the distribution

  - quantiles

    - represent equally spaced points in the CDF

    - ex: quintiles

      - income is often split between 20th, 40th, 60th, and 80th percentiles

### random numbers

  - replacement = a property of the sampling process

    - with replacement = same value can be chosen more than once

    - without replacement = once value is chosen, it must be removed from population

  - simple and efficient algorithm for generating random numbers with CDF

    - choose random x percentile rank from range 0-100

    - use Cdf.Percentile to find the value of x
