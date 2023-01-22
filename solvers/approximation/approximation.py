from abc import ABC, abstractmethod


class IApproximation(ABC):

    @abstractmethod
    def __call__(self, x: float, t: float, h: float) -> float:
        pass
