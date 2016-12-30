import nsfg, first, thinkstats2, thinkplot

def create_plot(hist):
    thinkplot.Hist(hist)
    thinkplot.Show(xlabel='weeks', ylabel='frequency')

def observe_outliers(hist):
    smallest = []
    for weeks, freq in hist.Smallest(10):
        smallest.append(weeks)
    print(smallest)

    largest = []
    for weeks, freq in hist.Largest(10):
        largest.append(weeks)
    print(sorted(largest))

def main(script):
    # read in data into dataframe
    preg = nsfg.ReadFemPreg()
    # use boolean Series to select rows from preg dataframe
    # return new dataframe with only births
    live = preg[preg.outcome == 1]

    # create a histogram of number of weeks of pregnancy
    # when live panda series is passed into Hist, any NaN values are dropped
    hist = thinkstats2.Hist(live.prglngth, label='Pregnancy Length')

    # create_plot(hist)
    observe_outliers(hist)

if __name__ == '__main__':
    import sys
    main(*sys.argv)
