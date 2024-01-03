# СОРТИРОВКА СЛИЯНИЕМ

# Идея: Исходный список делим на два до тех пор, пока не дойдем до списков из 1-го элемента. 
# Затем полученные элементы будем попарно соединять в упорядоченные списки из 2-х элементов. 
# Полученные списки из 2-х элементов будем попарно соединять в упорядоченные списки из 4-х элементов, 
# и так далее, пока не получим один упорядоченный список. 

def mergeSort(nums) : 
    if len(nums) > 1 : 
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right) : 
            if left[i] < right[j] : 
                nums[k] = left[i]
                i += 1
            else : 
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left) :
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right) :
            nums[k] = right[j]
            j += 1
            k += 1

list1 = [1, 5, 6, 9, 8, 7, 2, 1, 55, 2, 4]
mergeSort(list1)
print(list1)
    