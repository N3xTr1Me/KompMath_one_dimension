from abc import ABC, abstractmethod

import numpy as np

from grid.domain import Domain


class ISolver(ABC):

    @abstractmethod
    def solve(self, domain: Domain) -> np.ndarray:
        pass
