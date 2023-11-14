# import io, re
# with open('ГЛОБЭКС.TXT',"r") as gl:
#     # g=gl.read()
#     k=gl.readlines()
#     # print(gl.readline(100))
#     # print(g)
#     for stroka in k:
#         if "Почтовый адрес" in stroka:
#             ind=k.index(stroka)
#     print(k[ind+1])
import re


def search_info(fn, inf):
    with open(f"{fn}", "r") as gl:
        k = gl.readlines()
        for stroka in k:
            if f"{inf}" in stroka:
                cur_ind = k.index(stroka)
        if inf != "Телефон":
            cur_ind += 1
    return k[cur_ind].strip()


banks = [
    "ГЛОБЭКС.txt",
    "Ланта-Банк.TXT",
    "МОСОБЛБАНК.TXT",
    "РОСТ.TXT",
    "УРАЛСИБ.TXT",
    "ФИНПРОМБАНК.TXT",
]
types_inf = [
    "Сокращенное фирменное наименование кредитной организации",
    "Почтовый адрес",
    "Телефон",
]

for bank in banks:
    for type_inf in types_inf:
        print(search_info(bank, type_inf))
    print()
# print(search_info("ГЛОБЭКС.txt",'Телефон'))
# print(search_info("ГЛОБЭКС.txt",'Почтовый адрес'))
# print(search_info("ГЛОБЭКС.txt",'Сокращенное фирменное наименование кредитной организации'))
#     match= re.search("Почтовый адрес",g)
#     n=len("Почтовый адрес")
#     match2 = re.search("109004, Москва, ул.Земляной вал, д.59, стр.2", g)
#     if match:
#         start=match.start()
#         end=match.end()
#         print(end,match2.start())
#         gl.seek(end,0)
#         # print(gl.tell(),start,end,g[start:end])
#         # print()
#         # r = gl.tell()+3
#         # print()
#         # print(r)
#         print(g[end])
#         # gl.seek(end,1)
#         s=gl.readline()
#         print(s)
# #         print(g[match2.start():match2.end()])
# #         # print(start,s,g[end:end+100])
# # with open('ГЛОБЭКС.TXT',"r") as gl:
# #     for line in gl:
# #         print(line.rstrip("\n"))


# def search_info2(fn,inf):
#     with open(f'{fn}', "r") as gl:
#         k = gl.read()
#         match=re.search(f"{inf}",k)
#         if match:
#             print("ffffffffffffff")
#         st=(match.end())
#
#
#         gl.seek(st,0)
#         print(gl.tell())
#
#         ff=gl.readline()
#         print(len(ff))
#         print(gl.tell())
#
#         gl.seek(gl.tell(), 0)
#         print(gl.tell(),gl.readline())
#         # gl.seek(sl)
#         print(gl.readline())
#
#     #     for stroka in gl.readlines():
#     #         if f"{inf}" in stroka:
#     #             cur_ind = gl.readlines().index(stroka)
#     #     if inf!="Телефон":
#     #         cur_ind+=1
#     # return (gl.readlines()[cur_ind].strip())
# print(search_info2("ГЛОБЭКС.txt",'Почтовый адрес\n'))
# # plt.plot(x,y,c='g')
# # fig.autofmt_xdate()
