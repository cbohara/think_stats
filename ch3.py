import math, numpy as np, pandas as pd
import thinkstats2, thinkplot, nsfg, first, probability

def create_hist(df):
    # create a histogram of number of weeks of pregnancy
    return thinkstats2.Hist(df.prglngth, label='pregnancy Length')

def create_pmf(df):
    # create probability mass function (PMF)
    return thinkstats2.Pmf(df.prglngth, label='probability')

def prob_dict(hist):
    d = {}
    # total sample size
    n = hist.Total()
    # calculate and store probabilities into dictionary
    for x, freq in hist.Items():
        d[x] = freq / n
    return d

def display(pmf1, pmf2):
    thinkplot.PrePlot(2, cols=2)
    thinkplot.Hist(pmf1, align='right', width=0.45)
    thinkplot.Hist(pmf2, align='left', width=0.45)
    thinkplot.Config(xlabel='weeks', ylabel='probability', axis=[27, 46, 0, 0.6])
    thinkplot.PrePlot(2)
    thinkplot.SubPlot(2)
    thinkplot.Pmfs([pmf1, pmf2])
    return thinkplot.Show(xlabel='weeks', axis=[27, 46, 0, 0.6])

def zoom_in_around_mode(pmf1, pmf2):
    weeks = range(35, 46)
    diffs = []
    for week in weeks:
        p1 = pmf1.Prob(week)
        p2 = pmf2.Prob(week)
        diff = 100 * (p1 - p2)
        diffs.append(diff)
    thinkplot.Bar(weeks, diffs)
    return thinkplot.Show(xlabel='weeks', ylabel='difference in probability')

def bias_pmf(pmf, label):
    new_pmf = pmf.Copy(label=label)
    # for each class size
    for x, p in pmf.Items():
        # multiply the probability by the number of students who observe the class size
        new_pmf.Mult(x, x)
    new_pmf.Normalize()
    return new_pmf

def unbiased_pmf(pmf, label):
    new_pmf = pmf.Copy(label=label)
    # for each class size
    for x, p in pmf.Items():
        # divides each probability by the number of students who observe the class size
        new_pmf.Mult(x, 1.0/x)
    new_pmf.Normalize()
    return new_pmf

def pmf_mean(pmf):
    mean = 0.0
    for x, p in pmf.Items():
        mean += x * p
    return mean

def pmf_variance(pmf):
    mean = pmf_mean(pmf)
    variance = 0.0
    for x, p in pmf.Items():
        variance += p * (x - mean) ** 2
    print(variance)
    return variance

def main(script):
    # read in data into dataframe
    preg = nsfg.ReadFemPreg()

    # return new dataframe with only births
    live = preg[preg.outcome == 1]
    # create histogram
    live_hist = create_hist(live)
    # create basic dictionary of probabilities
    total_prob = prob_dict(live_hist)

    # split total live birth dataframe into first babies only dataframe
    firsts = live[live.birthord == 1]
    firsts_pmf = create_pmf(firsts)
    # and all others
    others = live[live.birthord != 1]
    others_pmf = create_pmf(others)

    # display graphs of probabilities
    # display(firsts_pmf, others_pmf)
    # # zoom in around mode to get a better idea of data pattern
    # zoom_in_around_mode(firsts_pmf, others_pmf)

    # given PMF, compute mean
    pmf_mean(firsts_pmf)
    # given PMF, compute variance
    pmf_variance(firsts_pmf)

    # unrelated example - class size paradox
    # dictionary of avg class size: frequency of classes offered
    d = {7: 8, 12: 8, 17: 14, 22: 4, 27: 6, 32: 12, 37: 8, 42: 3, 47: 2}
    # create pmf
    pmf = thinkstats2.Pmf(d, label='actual')
    # observe biased distribution
    biased_pmf = bias_pmf(pmf, label='observed')
    # thinkplot.PrePlot(2)
    # thinkplot.Pmfs([pmf, biased_pmf])
    # thinkplot.Show(xlabel='class size', ylabel='PMF')

if __name__ == '__main__':
    import sys
    main(*sys.argv)
