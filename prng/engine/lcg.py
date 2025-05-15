from typing import Optional

from prng.core import Base01Engine
from prng.util import seed_gen


class LCG(Base01Engine):
    """
    Linear Congruential Generator (LCG) for random numbers in [0, 1).
    """

    def __init__(self, seed: Optional[int] = None):
        """
        Constructor.
        :param seed: Initial seed value
        """
        if seed is None:
            seed = seed_gen()
        self.state = int(seed)
        self.a = 6364136223846793005
        self.c = 1442695040888963407
        self.m = 2 ** 64

    def __call__(self) -> float:
        """
        Generate next random number in [0, 1).
        """
        self.state = (self.a * self.state + self.c) % self.m
        return self.state / self.m
