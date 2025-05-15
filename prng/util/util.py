import os
from typing import Callable

import numpy as np
from scipy import optimize

SPLITMIX_VALS = np.array([0x9E3779B97F4A7C15, 0xBF58476D1CE4E5B9, 0x94D049BB133111EB], dtype=np.uint64)
"""
Consts for splitmix64 prng
"""


def invert_cdf(cdf: Callable[[float], float]) -> Callable[[float], float]:
    return lambda y: optimize.root_scalar(lambda x: cdf(x) - y, x0=0., method='secant').root


# def invert_cdf(cdf: Callable[[float], float], eps: float = 1e-6, expand_factor: float = 2, max_steps: int = 32):
#     """
#     Inverts a CDF function optimally: expanding only in the needed direction. SLOOW
#     """
#
#     def inverse_cdf(p: float) -> float:
#         if not (0. <= p <= 1.):
#             raise ValueError("p must be between 0 and 1 inclusive.")
#         lo, hi = 0., 1.
#         steps = 0
#         while steps < max_steps:
#             c_lo = cdf(lo)
#             c_hi = cdf(hi)
#             if c_lo <= p <= c_hi:
#                 break
#             if p < c_lo:
#                 width = hi - lo
#                 hi = lo
#                 lo -= width * expand_factor
#             elif p > c_hi:
#                 width = hi - lo
#                 lo = hi
#                 hi += width * expand_factor
#             steps += 1
#         if steps > max_steps:
#             raise ValueError("Failed to bracket value for inversion.")
#
#         while hi - lo > eps:
#             mid = (lo + hi) / 2
#             if cdf(mid) < p:
#                 lo = mid
#             else:
#                 hi = mid
#         return (lo + hi) / 2
#
#     return inverse_cdf


def seed_gen() -> np.uint64:
    """
    Random seed generator, uses random number provided by system.
    Slow, main use case is initializing prng based functions
    :return:
    """
    return np.uint64(int.from_bytes(os.urandom(8)))


def splitmix64(z: np.uint64) -> np.uint64:
    """
    Micro PRNG engine, primarily used for initializing large random states.
    :param z: current random number
    :return: new random number
    """

    z = np.uint64(z + SPLITMIX_VALS[0])
    z = np.uint64((z ^ (z >> 30)) * SPLITMIX_VALS[1])
    z = np.uint64((z ^ (z >> 27)) * SPLITMIX_VALS[2])
    return np.uint64(z ^ (z >> 31))
