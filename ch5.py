"""This file contains notes and code from Chapter 5."""

import scipy.stats
import thinkstats2
import thinkplot
import nsfg
import analytic


def eval_normal_cdf(x, mu=0, sigma=1):
    """Evaluate normal CDF and assume standard normal distribution as default."""
    return scipy.stats.norm.cdf(x, loc=mu, scale=sigma)


def make_normal_plot(weights, term_weights):
    """Generate normal probability plot from birthweight data."""
    # calculate mean and standard deviation for weight series
    mean = weights.mean()
    std = weights.std()

    xs = [-4, 4]
    # FitLine takes a sequence of xs, an intercept, and slope
    # returns fxs and fys = represents a line with the given parameters, evaluated at xs
    fxs, fys = thinkstats2.FitLine(xs, mean, std)
    thinkplot.Plot(fxs, fys, linewidth=4, color='0.8')

    thinkplot.PrePlot(2)
    # NormalProbability generates data for normal probability plot
    # returns numpy arrays xs and ys
    xs, ys = thinkstats2.NormalProbability(weights)
    thinkplot.Plot(xs, ys, label='all live')

    xs, ys = thinkstats2.NormalProbability(term_weights)
    thinkplot.Plot(xs, ys, label='full term')
    thinkplot.Show(root='analytic_birthwgt_normal',
                   title='Normal probability plot',
                   xlabel='Standard deviations from mean',
                   ylabel='Birth weight (lbs)')


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
    # test the distribution of birth weights for normality
    preg = nsfg.ReadFemPreg()
    full_term = preg[preg.prglngth >= 37]
    weights = preg.totalwgt_lb.dropna()
    term_weights = full_term.totalwgt_lb.dropna()
    make_normal_plot(weights, term_weights)


if __name__ == '__main__':
    import sys
    main(*sys.argv)
