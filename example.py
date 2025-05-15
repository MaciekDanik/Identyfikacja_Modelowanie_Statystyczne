import time

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm

from prng.distribution import PPFDist
from prng.engine import Xoshiro256p

rng = Xoshiro256p()
print(rng())
uni = PPFDist.from_cdf(norm.cdf)
xd = [uni.sample(rng) for _ in range(5000)]
plt.hist(xd, bins=25, density=True)
x = np.linspace(-5, 5, 1000)
plt.plot(x, norm.pdf(x), 'r-', lw=2, label='Rozkład normalny')
plt.show()
