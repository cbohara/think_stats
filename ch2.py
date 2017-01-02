import thinkstats2
import thinkplot
import nsfg
import math


def basic_hist(df):
    # create a histogram of number of weeks of pregnancy
    hist = thinkstats2.Hist(df.prglngth, label='Pregnancy Length')
    # display histogram
    thinkplot.Hist(hist)
    thinkplot.Show(xlabel='weeks', ylabel='frequency')


def outliers(df):
    # create a histogram of number of weeks of pregnancy
    hist = thinkstats2.Hist(df.prglngth, label='Pregnancy Length')

    # list the shortest pregnancy weeks
    smallest = []
    for weeks, freq in hist.Smallest(10):
        smallest.append(weeks)
    print("Smallest outliers:")
    print(smallest)

    # list the longest pregnancy weeks
    largest = []
    for weeks, freq in hist.Largest(10):
        largest.append(weeks)
    print("Largest outliers:")
    print(sorted(largest))


def comparison_hist(df1, df2):
    # create histograms
    firsts_hist = thinkstats2.Hist(df1.prglngth)
    others_hist = thinkstats2.Hist(df2.prglngth)

    # PrePlot takes the number of histograms we are planning to plot
    thinkplot.PrePlot(2)
    thinkplot.Hist(firsts_hist, align='right', width=0.45)
    thinkplot.Hist(others_hist, align='left', width=0.45)

    # display histogram focusing on pregnancies between 27 and 46 weeks
    thinkplot.Show(xlabel='weeks', ylabel='frequency', xlim=[27, 46])


def summary_statistics(df1):
    # uses pandas to calc mean
    mean = df1.prglngth.mean()
    print("Mean: " + str(mean))

    # use pandas to calc mode
    mode = df1.prglngth.mode()
    print("Mode: " + str(mode))

    # use pandas to calc variance (deviation from the mean squared)
    var = df1.prglngth.var()
    print("Variance: " + str(var))

    # use pandas to calc standard deviation (square root of variance)
    std = df1.prglngth.std()
    print("Standard deviation: " + str(std))


def cohen_effect_size(df1, df2):
    # difference between two groups / "pooled standard deviation"
    # calculate difference between means of the two groups
    diff = df1.prglngth.mean() - df2.prglngth.mean()

    # calculate variance for each group
    var1 = df1.prglngth.var()
    var2 = df2.prglngth.var()

    # number of inputs per group
    n1, n2 = len(df1.prglngth), len(df2.prglngth)

    # "pooled standard deviation"
    pooled = (n1 * var1 + n2 * var2) / (n1 + n2)

    # calculate cohen effect size
    d = diff / math.sqrt(pooled)
    print("Cohen Effect Size: " + str(d))
    return d


def main(script):
    # read in data into dataframe
    preg = nsfg.ReadFemPreg()

    # use boolean Series to select rows from original preg dataframe
    # return new dataframe with only births
    live = preg[preg.outcome == 1]

    # display histogram
    basic_hist(live)

    # print pregnancy length outliers
    outliers(live)

    # print pregnancy length summary statistics
    summary_statistics(live)

    # split total live birth dataframe into first babies only dataframe
    firsts = live[live.birthord == 1]
    # and all others
    others = live[live.birthord != 1]

    # plot both these dataframes in one histogram graph
    comparison_hist(firsts, others)

    # calculate cohen effect size
    cohen_effect_size(firsts, others)


if __name__ == '__main__':
    import sys
    main(*sys.argv)
