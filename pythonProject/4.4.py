set1=set()
set2=set()
# • выводить содержимое обоих списков на экран;
def print_set(s1,s2):
    print("Set_1: ",s1)
    print("Set_2: ",s2)
# • сортировать данные обоих списков;
def sort_set(s1,s2):
    # sortedsets=[sorted(s1),sorted(s2)]
    print("Set_1 sorted: ", sorted(s1))
    print("Set_2 sorted: ", sorted(s2))
    # return sortedsets
# • осуществлять поиск нужных записей в каждом из списков;
def search_set(s1,s2,item):
    found1=[i for i in s1 if item in i]
    found2=[i for i in s2 if item in i]
    print("foud in Set_1: ", found1)
    print("found in Set_2: ", found2)
# • добавлять записи в оба списка;
def add_to_set(s1,s2,item1,item2):
    s1.add(item1)
    s2.add(item2)
    # print("Set_1 after added : ", s1)
    # print("Set_2 after added : ", s2)
    return s1,s2
# • удалять записи из обоих списков;
def del_from_set(s1,s2,item):
    if item in s1 and item in s2:
        s1.remove(item)
        s2.remove(item)
    elif item in s1:
        s1.remove(item)
    elif item in s2:
        s2.remove(item)
    else:
        print('No ',item,' in set1 and set2...')
        return
    print("Set_1 after del : ", s1)
    print("Set_2 after del : ", s2)

# • находить записи, которые содержатся в обоих списках;
def find_in_both(s1,s2):
    items=s1.intersection(s2)
    print('записи, которые содержатся в обоих списках: ',items)
# • удалять из второго списка те записи, которые содержатся в обоих списках;
def del_findinboth_froms2(s1,s2):

    print("Set_2 befor del : ", s2)
    s2=s2.difference(s1)
    print("Set_2 after del : ", s2)
# • находить записи в одном списке, которые отсутствуют в другом списке
def find_in_s(s1,s2):
    uniq_s1=s1.difference(s2)
    uniq_s2=s2.difference(s1)
    print('Уникально в 1 множестве: ', uniq_s1)
    print('Уникально вo 2 множестве: ', uniq_s2)

set1,set2=add_to_set(set1,set2,"значение1", "значение2")
set1,set2=add_to_set(set1,set2,"значение3", "значение4")


print_set(set1,set2)

# s1,s2=sort_set(set1,set2)
# print_set(s1,s2)


set1,set2=add_to_set(set1,set2,"значение4", "значение3")
print_set(set1,set2)

del_from_set(set1,set2,"значение4",)
# print_set(set1,set2)

search_set(set1,set2,"значение3")

find_in_both(set1,set2)
del_findinboth_froms2(set1,set2)

find_in_s(set1,set2)