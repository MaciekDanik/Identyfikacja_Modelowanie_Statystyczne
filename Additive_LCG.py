class Additive_LCG:
    #a = 1103515245 //mnożnik
    #c = 12345 //przyrost
    #m = 2**32 //moduł
    def __init__(self, seed, a = 1103515245, c = 12345, m = 2**32):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m

    def generate(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed / self.m
    
    def generate_n(self, n, Low_end = 0.0, High_end = 1.0):
        result = []
        for i in range (n):
            num_0_1 = self.generate()

            num_scaled = Low_end + num_0_1 * (High_end - Low_end)
            result.append(num_scaled)
        return result
    
    