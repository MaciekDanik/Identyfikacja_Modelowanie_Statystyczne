import os
import numpy as np

def seed_gen() -> np.uint64:
    """
    Random seed generator, uses random number provided by system.
    Slow, main use case is initializing prng based functions
    :return:
    """
    return np.uint64(int.from_bytes(os.urandom(8)))