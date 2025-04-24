import matplotlib.pyplot as plt

def plot_numbers(nums, title="Rozkład jednostajny"):
    plt.figure(figsize=(10,6))
    plt.plot(range(len(nums)), nums, marker='o', linestyle='', linewidth=0.5, markersize=3)
    plt.xlabel("Indeks")
    plt.ylabel("Wartość")
    plt.title(title)
    plt.grid(True)
    plt.show()