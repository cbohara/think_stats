"""This file contains notes and code from Chapter 5."""

import thinkstats2
import thinkplot
import analytic

def main(script):
    # read in data about the births of 44 kids on the same day from babyboom.dat
    # df with columns for time, sex, weight_g, and minutes (since midnight)
    df = analytic.ReadBabyBoom()
    # difference between consecutive birth times
    diffs = df.minutes.diff()
    # distribution of the interarrival times
    cdf = thinkstats2.Cdf(diffs, label='actual')
    thinkplot.Cdf(cdf)
    # thinkplot.Show(xlabel='minutes', ylabel='CDF')

    # plot CCDF (complementary CDF) to observe if distribution is exponential
    thinkplot.Cdf(cdf, complement=True)
    # not straight = exponential distribution is not perfect for this model
    thinkplot.Show(xlabel='minutes', ylabel='CCDF', yscale='log')


if __name__ == '__main__':
    import sys
    main(*sys.argv)
