class Generator:
    def __init__(self, seed1, seed2, seed3, a1 = 1176, a2 = 1476, a3 = 1776, m = (2**35) - 5):
        self.U = [seed1, seed2, seed3]
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.m = m 

    def generate(self):
        res = (self.a1 * self.U[0] + self.a2 * self.U[1] + self.a3 * self.U[2]) % self.m
        
        self.U[2] = self.U[1]
        self.U[1] = self.U[0]
        self.U[0] = res

        res = res/self.m
        return res
    
    def generate_n(self, n, Low_end = 0.0, High_end = 1.0):
        result = []
        for i in range (n):
            num_0_1 = self.generate()

            num_scaled = Low_end + num_0_1 * (High_end - Low_end)
            result.append(num_scaled)
        return result