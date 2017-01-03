"""This file contains notes and code from Chapter 4."""

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

def main(script):
    scores = [55, 66, 77, 88, 99]
    your_score = 88
    percentile_rank(scores, your_score)
    percentile(scores, 80)


if __name__ == '__main__':
    import sys
    main(*sys.argv)
