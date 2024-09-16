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
    l1 = [5,4,0,4,4]
    l2 = [1,4,1,0,8]
    l3 = [7,9,2,9,4]
    l4 = [2,9,6,4,9]
    l5 = [2,5,2,6,0]
    l6 = [6,0,6,6,0]
    l7 = [2,9,9,5]
    l8 = [5,3,7,7,7]
    l9 = [4,9,6,8,9]   
    l10 = [9,0,8,3]
    
    test_lists = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]
    
    for test_list in test_lists:
        sorted_list, inversions = mergesort(test_list)
        print(f"Sorted list: {sorted_list}, Inversions: {inversions}")
    
    # Test another case
    lyst = [1, 4, 6, 3, 2, 9, 5, 12, 10, 11, 7, 13, 8, 15, 14]
    sorted_list, inversions = mergesort(lyst)
    print(f"Sorted list: {sorted_list}, Inversions: {inversions}")


if __name__ == '__main__':
    main()