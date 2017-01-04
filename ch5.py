"""This file contains notes and code from Chapter 5."""

import scipy.stats
import thinkstats2
import thinkplot
import analytic


def eval_normal_cdf(x, mu=0, sigma=1):
    """Evaluate normal CDF and assume standard normal distribution as default."""
    return scipy.stats.norm.cdf(x, loc=mu, scale=sigma)


def make_normal_plot(weights):
    """Generate normal probability plot from birthweight data."""
    mean = weights.mean()
    std = weights.std()
    # plot from -4 to 4 standard deviations from the mean
    xs = [-4, 4]
    # FitLine to given data, returns tuple of numpy array
    fxs, fys = thinkstats2.FitLine(xs, inter=mean, slope=std)
    thinkplot.Plot(fxs, fys, color='gray', label='model')

    xs, ys = thinkstats2.NormalProbability(weights)
    thinkplot.Plot(xs, ys, label='birth weights')
    thinkplot.Show(xaxis='adult weight', yaxis='CDF')


def main(script):
    # read in data about the births of 44 kids on the same day from babyboom.dat
    # df with columns for time, sex, weight_g, and minutes (since midnight)
    df = analytic.ReadBabyBoom()

    # exponential distribution
    # difference between consecutive birth times
    diffs = df.minutes.diff()
    # distribution of the interarrival times
    cdf = thinkstats2.Cdf(diffs, label='actual')
    thinkplot.Cdf(cdf)
    # thinkplot.Show(xlabel='minutes', ylabel='CDF')
    # plot CCDF (complementary CDF) to observe if distribution is exponential
    thinkplot.Cdf(cdf, complement=True)
    # not straight = exponential distribution is not perfect for this model
    # thinkplot.Show(xlabel='minutes', ylabel='CCDF', yscale='log')

    # standard normal distribution
    standard_normal = eval_normal_cdf(0)
    # test to determine if normal distribution is an appropriate model
    # NormalProbability() returns 2 numpy arrays
    # xs contains random values from the standard normal distribution
    # ys contains sorted values from the sample
    # xs, ys = thinkstats2.NormalProbability(sample)

    weights = df['weight_g']
    # generates standard normal plot
    make_normal_plot(weights)


if __name__ == '__main__':
    import sys
    main(*sys.argv)
