import unsortedlist
import pivotstrategy

"""
1. Choose pivot: first/last/median/random
2. Partition array:
3. Sorting
    a) elements smaller than pivot move left
    b) elements greater than pivot move right
    c) place pivot
4. Recursive call of quicksort
5. Base case: Recurstion stops when there is only one more element in the sub-array

Doesn't work with duplicates!!!
"""
class Quicksort:
    def __init__(self, array, pivot_strategy):
        self.pivot_strategy = pivot_strategy
        self.array = array.copy()


    def partition(self, low, high):
        """Divide and conquer"""

        pivot = self.pivot_strategy.select_pivot(self.array, low, high)     # get pivot

        pivot_index = low 
        for i in range(low, high+1):    # base case
            if self.array[i] == pivot:
                pivot_index = i
                break

        self.array[pivot_index], self.array[high] = self.array[high], self.array[pivot_index]  # swap pivot with last element

        i = low - 1
        for j in range(low, high):
            if self.array[j] < pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]

        pivot_final_pos = i + 1
        self.array[pivot_final_pos], self.array[high] = self.array[high], self.array[pivot_final_pos]
        return pivot_final_pos
    
    def _sort(self, low, high):
        if low < high:
            pivot_position = self.partition(low, high)

            self._sort(low, pivot_position - 1)
            self._sort(pivot_position + 1, high)
    
    def sort(self):
        self._sort(low=0, high=len(self.array) - 1)
        return self.array

    
if __name__ == '__main__':
    l1 = unsortedlist.l1

    p1 = pivotstrategy.RandomElementPivot()
    
    q = Quicksort(l1, p1)
    sorted_array = q.sort()
    print(f"Unsorted array: \n{l1}")
    print("===============================================================================")
    print(f"Sorted array: \n{sorted_array}")