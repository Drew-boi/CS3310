import sys

def merge(lyst1 : list, lyst2 : list ) -> list:
    m = len(lyst1)
    l = len(lyst2)
    k = 0
    j = 0
    inversions = 0 
    returnList = []
    while k < m or j < l:
        if k < m and j < l:
            if lyst1[k] <= lyst2[j]:
                returnList.append(lyst1[k])
                k += 1
            elif lyst2[j] < lyst1[k]: # Inversion case   
                inversions += m - k # Every number after lyst1[k] is also an inversion
                returnList.append(lyst2[j])
                j += 1 
            else:
                continue
        
        elif k < m:
            returnList.append(lyst1[k])
            k += 1
        
        elif j < l:
            returnList.append(lyst2[j])
            j += 1
    return returnList, inversions

def mergesort(lyst, inversions = 0):
    n = len(lyst)
    if n == 1:
        return lyst, 0 # Base case, one element and no inversions
    halfn = n//2
    lyst1, inversions1 = mergesort(lyst[:halfn])
    lyst2, inversions2 = mergesort(lyst[halfn:])
    lyst, inversions3 = merge(lyst1, lyst2)
    inversions += inversions1 + inversions2 + inversions3
    return lyst, inversions

def main():
    # commandline: python3 CountingInversions.txt (filename)
    try:
        filename = sys.argv[1]
        print(filename)
    except IndexError:
        print("Usage: python3 CountingInversions.txt <filename>")
        return
    with open(filename) as f:
        test_lists = []
        for line in f:
            line = line.strip()
            char_array = [c for c in line]
            test_lists.append(char_array)
    for test_list in test_lists:
        # print(f"Unsorted List: {test_list}", end="   ") # use this line if you want to check the unsorted list
        sorted_list, inversions = mergesort(test_list)
        print(f"Sorted list: {sorted_list}, Inversions: {inversions}")
    
    # Test another case
    lyst = [1, 4, 6, 3, 2, 9, 5, 12, 10, 11, 7, 13, 8, 15, 14]
    sorted_list, inversions = mergesort(lyst)
    print(f"Sorted list: {sorted_list}, Inversions: {inversions}")


if __name__ == '__main__':
    main()