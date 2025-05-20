import matplotlib.pyplot as plt

def plot_numbers(nums, title="Rozkład jednostajny"):
    plt.figure(figsize=(10,6))
    plt.plot(range(len(nums)), nums, marker='o', linestyle='', linewidth=0.5, markersize=3)
    plt.xlabel("Indeks")
    plt.ylabel("Wartość")
    plt.title(title)
    plt.grid(True)
    plt.show()

def plot_two_sets(nums1, nums2, title="Porównanie rozkładów", label1="Zbiór 1", label2="Zbiór 2"):
    """
    Wyświetla dwie listy liczb na jednym wykresie, używając różnych kolorów.

    Args:
        nums1 (list): Pierwsza lista liczb do wyświetlenia.
        nums2 (list): Druga lista liczb do wyświetlenia.
        title (str, optional): Tytuł wykresu. Domyślnie "Porównanie rozkładów".
        label1 (str, optional): Etykieta dla pierwszej listy. Domyślnie "Zbiór 1".
        label2 (str, optional): Etykieta dla drugiej listy. Domyślnie "Zbiór 2".
    """
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(nums1)), nums1, marker='o', linestyle='', linewidth=0.5, markersize=3, color='blue', label=label1)
    plt.plot(range(len(nums2)), nums2, marker='x', linestyle='', linewidth=0.5, markersize=3, color='red', label=label2)
    plt.xlabel("Indeks")
    plt.ylabel("Wartość")
    plt.title(title)
    plt.grid(True)
    plt.legend()  # Dodaje legendę, aby odróżnić zbiory
    plt.show()