from abc import ABC, abstractmethod

class SortInterface(ABC):

    @abstractmethod
    def sort(self, array, callback=None) -> int:
        pass
    
    @abstractmethod
    def display_bars(self, array, sub_array=None):
        pass