from abc import ABC, abstractmethod


class Base01Engine(ABC):
    """
    Supplier of random numbers from [0,1) interval
    """

    @abstractmethod
    def __call__(self) -> float:
        """
        Generates random number
        :return: random number 0 <= x < 1
        """
        pass


class BaseIntEngine(ABC):
    """
    Supplier of random int numbers
    """

    @abstractmethod
    def __call__(self) -> int:
        """
        Generates random number
        :return: random number 0 <= x < 1
        """
        pass
