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
