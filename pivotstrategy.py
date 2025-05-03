import unsortedlist
import random
from abc import ABC, abstractmethod

l1 = unsortedlist.l1



class PivotStrategy(ABC):
    """Pivot strategies for sorting algorithms"""

    @abstractmethod
    def select_pivot(self, array, low, high):
        pass

class FirstElementPivot(PivotStrategy):
    def select_pivot(self, array, low, high):
        return array[low]

class LastElementPivot(PivotStrategy):
    def select_pivot(self, array, low, high):
        return array[high]

class MedianElementPivot(PivotStrategy):
    def select_pivot(self, array, low, high):
        return array[(low + high) // 2]
    
class RandomElementPivot(PivotStrategy):
    def select_pivot(self, array, low, high):
        return array[random.randint(low, high)]