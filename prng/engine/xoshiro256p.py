from typing import Optional

import numpy as np
from numpy.typing import NDArray

from ..core.base_engine import Base01Engine
from ..util import splitmix64, seed_gen

np.seterr(over='ignore')


class Xoshiro256p(Base01Engine):
    """
    Xoshiro256+ engine. 256 bit state, based on xor, shift and rotate operations
    """

    def __init__(self, seed: Optional[np.uint64] = None):
        """
        Constructor
        :param seed: initial seed
        """
        if seed is None:
            seed = seed_gen()
        self._s: NDArray[1, np.uint64] = np.zeros(4, dtype=np.uint64)
        self._s[0] = splitmix64(seed)
        self._s[1] = splitmix64(self._s[0])
        self._s[2] = splitmix64(self._s[1])
        self._s[3] = splitmix64(self._s[2])

    @staticmethod
    def _rotl(x: np.uint64, k: int) -> np.uint64:
        return (x << k) | (x >> (64 - k))

    def next(self) -> np.uint64:
        result = self._rotl(self._s[0] + self._s[3], 23) + self._s[0]
        t = self._s[1] << np.uint64(17)

        self._s[2] ^= self._s[0]
        self._s[3] ^= self._s[1]
        self._s[1] ^= self._s[2]
        self._s[0] ^= self._s[3]

        self._s[2] ^= t

        self._s[3] = self._rotl(self._s[3], 45)
        return result

    def __call__(self) -> float:
        return (self.next() >> np.uint64(11)) * (1.0 / (1 << 53))
