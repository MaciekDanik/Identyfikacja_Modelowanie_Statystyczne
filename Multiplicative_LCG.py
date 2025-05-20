from typing import Optional
from util import seed_gen

class Multiplicative_LCG:
    def __init__(self, seed: Optional[int] = None, a = 1103515245, m = 2**32):
        if seed is None:
            self.seed = seed_gen()
        self.state = seed
        self.a = a
        self.m = m

    def generate(self):
        self.state = (self.a * self.state) % self.m
        return self.state / self.m
    
    def generate_n(self, n, Low_end = 0.0, High_end = 1.0):
        result = []
        for i in range (n):
            num_0_1 = self.generate()

            num_in_range = Low_end + num_0_1 * (High_end - Low_end)
            result.append(num_in_range)
        return result
    
    def __call__(self):
        return self.generate()
    
    