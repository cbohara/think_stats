import nsfg, first, thinkstats2, thinkplot

def create_basic_histo(hist):
    # create a histogram of number of weeks of pregnancy
    hist = thinkstats2.Hist(live.prglngth, label='Pregnancy Length')

    # display histogram
    thinkplot.Hist(hist)
    thinkplot.Show(xlabel='weeks', ylabel='frequency')

def observe_outliers(hist):
    # list the shortest pregnancy weeks
    smallest = []
    for weeks, freq in hist.Smallest(10):
        smallest.append(weeks)
    print(smallest)

    # list the longest pregnancy weeks
    largest = []
    for weeks, freq in hist.Largest(10):
        largest.append(weeks)
    print(sorted(largest))

def create_comparison_histo(firsts, others):
    # create histograms
    first_hist = thinkstats2.Hist(firsts.prglngth)
    others_hist = thinkstats2.Hist(others.prglngth)

    # display info
    # PrePlot takes the number of histograms we are planning to plot
    thinkplot.PrePlot(2)
    thinkplot.Hist(first_hist, align='right', width=0.45)
    thinkplot.Hist(others_hist, align='left', width=0.45)

    # display histogram focusing on pregnancies between 27 and 46 weeks
    thinkplot.Show(xlabel='weeks', ylabel='frequency', xlim=[27,46])

def main(script):
    # read in data into dataframe
    preg = nsfg.ReadFemPreg()
    # use boolean Series to select rows from preg dataframe
    # return new dataframe with only births
    live = preg[preg.outcome == 1]

    # display histogram
    # create_basic_histo(hist)

    # print outliers
    # observe_outliers(hist)

    # split total live birth dataframe into first babies only dataframe
    firsts = live[live.birthord == 1]
    # and all others
    others = live[live.birthord != 1]

    # plot both these dataframes in one histogram graph
    create_comparison_histo(firsts, others)


if __name__ == '__main__':
    import sys
    main(*sys.argv)
