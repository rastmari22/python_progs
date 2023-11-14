# startList=["Сергей","Ольга","Юрий","Сергей","Александр"]
#
# print(sorted(set(startList),reverse=True))

li=["Сергей","Ольга","Юрий","Сергей","Александр"]

print("Отсортированный список: ", sorted(set(li),key=lambda a: len(a)))


