import csv
def read_from_file(fn):
    with open(f"{fn}") as file:
        for line in file:
            dd = csv.reader(file, delimiter=";")
            data = list(dd)
    print(f"Файл {fn} считан ")
    return data
def num_to_int(dat):
    for str_data in dat:
        str_data[0]=int(float(str_data[0]))
    print(f"Данные преобразованы ")
    return dat

def change_name(data):
    for para in data:
        para[0],para[1]=para[1],para[0]
    return data
def sort_num(data, k):
    sort_data=sorted((data),key=lambda a: a[0])
    if k=='numb':
        print(f"Даннфе отсортированы по номеру банка")
    if k=='name':
        print(f"Даннфе отсортированы по наименованию банка")
    return sort_data
def sort_to_file(data,fn):
    with open(f"{fn}",'w', newline='') as file:
        f=csv.writer(file)
        f.writerows(data)
    print(f"Данные записаны в файл {fn}")


# data=read_from_file("NAMES.txt")
# # data=num_to_int(data)
# numbers=[str_data[0] for str_data in data]
# numbers=list(map(int,list(map(float,numbers))))
#
#
# print(numbers)
data=read_from_file("NAMES.txt")
data=num_to_int(data)
# print(data)
data=sort_num(data,'numb')
# print(data)
sort_to_file(data,"NAMES_sort_numb.txt")
change_name(data)
# print(data)
data=sort_num(data,'name')
# print(data)
sort_to_file(data,"NAMES_sort_name.txt")