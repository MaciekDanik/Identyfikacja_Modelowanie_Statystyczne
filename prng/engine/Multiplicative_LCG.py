class Multiplicative_LCG:
    def __init__(self, seed, a = 1103515245, m = 2**32):
        self.seed = seed
        self.a = a
        self.m = m

    def generate(self):
        self.seed = (self.a * self.seed) % self.m
        return self.seed / self.m
    
    def generate_n(self, n, Low_end = 0.0, High_end = 1.0):
        result = []
        for i in range (n):
            num_0_1 = self.generate()

            num_in_range = Low_end + num_0_1 * (High_end - Low_end)
            result.append(num_in_range)
        return result
    
    def __call__(self):
        return self.generate()
    
    