import math
from numbers import Number
from typing import Callable

from ..util import Random01Supplier
from ..util import invert_cdf


class PPFDist:
    """Distribution based on probability point function function."""

    def __init__(self, ppf: Callable[[float], Number]):
        """
        Constructor
        :param ppf: Probability point function, inverse of CDF
        """
        self._ppf = ppf

    def sample(self, prng: Random01Supplier) -> Number:
        return self._ppf(prng())

    @classmethod
    def from_cdf(cls, cdf: Callable[[float], float]) -> "PPFDist":
        """
        Factory method for creating instance using CDF.
        :param cdf: Cumulative distribution function
        :return: Distribution instance
        """
        icdf = invert_cdf(cdf)
        return PPFDist(icdf)

    @classmethod
    def uniform_int_distribution(cls, a, b) -> "PPFDist":
        """
        Factory method for creating uniform integer distribution from [a,b) interval.
        :param a: lower bound (inclusive)
        :param b: upper bound (exclusive)
        :return: Distribution instance
        """
        return PPFDist(lambda rand: a + math.floor(rand * (b - a)))
