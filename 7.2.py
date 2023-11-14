
def read_array_from_file(fn):
    arr=[]
    with open(f"{fn}") as file:
        for line in file:
            arr.append([int(x) for x in line.split()])
    print(f'Массив считан из файла {fn}')
    if len(arr)==1:
        return list(*arr)
    return arr

arr1=read_array_from_file('first_arr.txt')
print(arr1)
arr2=read_array_from_file('second_arr.txt')
print(arr2)

def new_array(ar1,ar2):
    na=[]
    na.append([e1+e2 for e1,e2 in (zip(ar1,ar2))])
    na.append([e1 - e2 for e1, e2 in (zip(ar1, ar2))])
    na.append([e1 * e2 for e1, e2 in (zip(ar1, ar2))])
    return na

new_arr=(new_array(arr1,arr2))

def new_array_to_file(arr):
    with open('result_array.txt','w+') as ra:
        for el in arr:
            list_el = (list(map(str, el)))
            ra.write((" ".join(list_el))+"\n")
    return "Результирующий массив записан в файл"
new_array_to_file(new_arr)
import numpy as np
arr1=read_array_from_file('result_array.txt')
print(np.array(arr1))