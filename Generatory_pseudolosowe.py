from Additive_LCG import Additive_LCG
from Multiplicative_LCG import Multiplicative_LCG
from ploting import plot_numbers
import matplotlib.pyplot as plt


if __name__ == "__main__":
    add_lcg = Additive_LCG(1)
    mult_lcg = Multiplicative_LCG(1)

    numbers = add_lcg.generate_n(300)
    numbers_1 = mult_lcg.generate_n(300)

    plt.ion()
    plot_numbers(numbers, "Rozkład jednostajny w zakresie [-3,3] -- addytywny LCG")
    plot_numbers(numbers_1, "Rozkład jednostajny w zakresie [-3,3] -- multiplikatywny LCG")
    plt.ioff()

    input("Naciśnij 'Enter' aby zamknąć wykresy...")
