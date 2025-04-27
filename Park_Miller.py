class Park_Miller:
    #inne warianty a i m (stosowane w praktyce):
    # a = 75 (pierwiastek pierwotny modulo F_4)  m = 2**16 (liczba pierwsza fermata F_4)
    # a = 16807 (pierwiastek pierwotny modulo M_31)  m = 2**31 - 1 (liczba pierwsza Mersenn'a M_31)
    # a = 44485709377909  m = 2**48
    # a = 279470273  m = 4294967291
    def __init__(self, seed, a = 16807, m = (2**31 -1)):
        self.seed = seed
        self.a = a
        self.m = m

    def generate(self): 
        self.seed = (self.a * self.seed) % self.m #losuje liczbę z przedziału [1, m-1]

        return self.seed / self.m #skaluje liczbę do zakresu [0,1)
    
    def generate_n(self, n, Low_end = 0.0, High_end = 1.0):
        result = [0]

        for i in range(n):
            num_0_1 = self.generate()
            num_scaled = Low_end + num_0_1 * (High_end - Low_end)

            result.append(num_scaled)
        return result