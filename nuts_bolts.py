from typing import List
# Partitioning function, pivot can be passed
def partition(arr: List[str], start: int, end: int, pivot: str) -> int:
    i = start
    j = start
    while j < end:
        if (arr[j] < pivot):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        elif (arr[j] == pivot):
            arr[j], arr[end] = arr[end], arr[j]
            j -= 1
        j += 1
    arr[i], arr[end] = arr[end], arr[i]
    # Return partition index of an array based on the pivot element of other array.
    return i
# Function which works just like quick sort
def matchPairs(nuts: List[str], bolts: List[str], start: int, end: int) -> None:
    if (start < end):
        # Choose last character of bolts array as a pivot for nuts partition.
        pivot = partition(nuts, start, end, bolts[end])
 
        # Now choose nuts pivot returned previously for bolts partitioning.
        partition(bolts, start, end, nuts[pivot])
 
        # Recur for for the subarrays of nuts and bolts.
        matchPairs(nuts, bolts, start, pivot - 1)
        matchPairs(nuts, bolts, pivot + 1, end)
# Driver code
if __name__ == "__main__":
    # Nuts and bolts are represented
    # as array of characters
    nuts  = ['^', '$', '@', '#', '%', '&']
    bolts = ['$', '%', '&', '^', '@', '#']
    print("Unmatched nuts and bolts:")
    print("nuts:" , nuts)
    print("bolts:" , bolts)
    # Method based on quicksort() which maps nuts to corresponding bolts
    matchPairs(nuts, bolts, 0, len(nuts)-1)
    print("Matched nuts and bolts are : ")
    print("nuts:" , nuts)
    print("bolts:" , bolts)
   
        