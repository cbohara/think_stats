"""This file contains notes and code from Chapter 4."""

import thinkstats2
import thinkplot
import first
import numpy as np


def percentile_rank(scores, your_score):
    """ Return percentile rank of your test score."""
    count = 0
    for score in scores:
        if score <= your_score:
            count += 1

    percentile_rank = 100.0 * count / len(scores)
    return percentile_rank


def percentile(scores, your_rank):
    """ Return score based on percentile rank."""
    scores.sort()
    for score in scores:
        if percentile_rank(scores, score) >= your_rank:
            return score


def eval_cdf(sample, x):
    """ Compute cumulative distribution function (CDF) for any given value (x)."""
    count = 0
    for value in sample:
        if value <= x:
            count += 1

    probability = count / len(sample)
    return probability


def position_to_percentile(position, field_size):
    """ Given position completed race, determine percentile rank."""
    beat = field_size - position + 1
    percentile = 100.0 * beat / field_size
    return percentile


def percentile_to_position(percentile, field_size):
    """ Given percentile rank, determine position in race."""
    beat = percentile * field_size / 100.0
    position = field_size - beat + 1
    return position


def main(script):
    scores = [55, 66, 77, 88, 99]
    your_score = 88
    # return percentile rank your score falls into within the scores list
    percentile_rank(scores, your_score)
    # return percentile = value associated with a given percentile rank
    percentile(scores, 80)

    sample = [1, 2, 2, 3, 5]
    # returns percentile rank of 5 within sample list
    eval_cdf(sample, 5)

    # apply CDF to pregnancy data
    live, firsts, others = first.MakeFrames()
    cdf = thinkstats2.Cdf(live.prglngth, label='prglngth')
    thinkplot.Cdf(cdf)
    # thinkplot.Show(xlabel='weeks', ylabel='CDF')

    # compare distribution between first and subsequent pregnancies
    first_cdf = thinkstats2.Cdf(firsts.totalwgt_lb, label='first')
    other_cdf = thinkstats2.Cdf(others.totalwgt_lb, label='other')
    thinkplot.PrePlot(2)
    thinkplot.Cdfs([first_cdf, other_cdf])
    # thinkplot.Show(xlabel='weight(lbs)', ylabel='CDF')

    # calculate percentile rank of birth weights
    weights = live.totalwgt_lb
    cdf = thinkstats2.Cdf(weights, label='totalwgt_lb')
    # generate random sample
    sample = np.random.choice(weights, 100, replace=True)
    # compute percentile rank of each value in sample and populate ranks list
    ranks = [cdf.PercentileRank(x) for x in sample]
    # plot CDF of percentile ranks for a random sample of birth weights
    rank_cdf = thinkstats2.Cdf(ranks)
    thinkplot.Cdf(rank_cdf)
    # thinkplot.Show(xlabel='percentile rank', ylabel='CDF')
    # generate random values with a given CDF
    thinkstats2.Cdf.Random(rank_cdf)

    # find my percentile rank in the distribution
    other_weights = others.totalwgt_lb
    other_cdf = thinkstats2.Cdf(others.totalwgt_lb, label='totalwgt_lb')
    # generate random sample
    other_sample = np.random.choice(other_weights, 100, replace=True)
    # compute percentile rank of each value in sample and populate ranks list
    other_ranks = [cdf.PercentileRank(x) for x in other_sample]
    # determine percentile rank for my birth weight
    percentile_rank(other_ranks, 8)


if __name__ == '__main__':
    import sys
    main(*sys.argv)
