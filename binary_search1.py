def search_ele (array,search,start,end) :
    mid=(start+end) // 2
    if search == array[mid] :
        print(start,"found at",array[mid])
    elif search < array[mid] :
        search_ele(array,search,start,mid-1) 
    elif search > array[mid] :
        search_ele(array,search,mid+1,end)
array=[1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29, 14 ,89,56,22,77,44,51,268,886,51,74,76,12]
array.sort()
print(array)
array.pop(3)
array.remove(12)
print(array)
search=77
start=0
end=len(array)
print(end)
search_ele(array,search,start,end)