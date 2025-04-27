from Additive_LCG import Additive_LCG
from Multiplicative_LCG import Multiplicative_LCG
from generator_z_wykladu import Generator
from Park_Miller import Park_Miller
from ploting import plot_numbers
import matplotlib.pyplot as plt


if __name__ == "__main__":
    add_lcg = Additive_LCG(123)
    mult_lcg = Multiplicative_LCG(1)
    gen = Generator(1, 2, 3)
    pm = Park_Miller(123)

    results_add_lcg = add_lcg.generate_n(2500)
    results_mult_lcg = mult_lcg.generate_n(30)
    results_gen = gen.generate_n(2500)
    results_pm = pm.generate_n(2500)

    plt.ion()
    plot_numbers(results_add_lcg, "Rozkład jednostajny -- addytywny LCG")
    # plot_numbers(results_mult_lcg, "Rozkład jednostajny -- multiplikatywny LCG")
    # plot_numbers(results_gen, "Rozkład jednostajny -- generator z wykładu")
    plot_numbers(results_pm, "Rozkład jednostajny -- generator Park-Miler")
    plt.ioff()

    input("Naciśnij 'Enter' aby zamknąć wykresy...")
