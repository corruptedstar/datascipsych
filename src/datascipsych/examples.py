"""Module with example functions."""

import numpy as np


def hello():
    """Print a greeting."""
    print("Hello world.")


def ismissing(responses):
    """Check if responses are n/a."""
    return np.asarray(responses) == "n/a"

def is_outlier(col):
    """Return an expression to evaluate whether elements of a column are outliers."""
    q1 = col.quantile(0.25)
    q3 = col.quantile(0.75)
    iqr = q3 - q1
    return (col < q1 - 1.5 * iqr) | (col > q3 + 1.5 * iqr)