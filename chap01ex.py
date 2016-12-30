"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def read_fem_resp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows=None):
    """
    reads the NSFG respondent data
    returns dataframe
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    return df

def validate_pregnum(resp):
    """
    validates pregnum in response file
    input response is respondent dataframe
    """
    # read pregnancy frame
    preg = nsfg.ReadFemPreg()
    # make the map from caseid to list of pregnancy indices
    preg_map = nsfg.MakePregMap(preg)
    # iterate through pregnum series
    for index, pregnum in resp.pregnum.iteritems():
        caseid = resp.caseid[index]
        indices = preg_map[caseid]
        # check pregnum from respondent files equals the number of records in the pregnancy file
        if len(indices) != pregnum:
            print(caseid, len(indices), pregnum)
            return False
    return True

def main(script):
    """
    tests the functions in this module
    """
    resp = read_fem_resp()

    assert(len(resp) == 7643)
    assert(resp.pregnum.value_counts()[1] == 1267)
    assert(validate_pregnum(resp))

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
