import random

import matplotlib.pyplot as plt
import csv
from datetime import datetime
import re

# import numpy as np
# # plt.style.use('_mpl-gallery')
# date_list=[]
# close_list=[]
# high_list=[]
# data=[['ff','ss','tt'],[1,2,3],[4,5,6]]
# wanted=input("Введите желаемые данные open/close/high/low: ")

def open_file(fn,want):
    with open(f"{fn}") as file:
        data=csv.reader(file,delimiter=";")
        data_list=list(data)

        name_data=[re.sub(r'[<> ]', '', m) for m in data_list[0]]
        # dm = dict.fromkeys(name_data, [])
        # print(dm)
        # dm2={elem: ind for ind,elem in enumerate(name_data)}
        # print(dm2)

        dd={name_data[i]:[sublist[i] for sublist in data_list[1:]]for i in range(len(data_list[0]))}
        # print(dd)
        want_mas=[dd[i] for i in want]
        for el in want_mas:
            want_mas[want_mas.index(el)]=list(map(float,el))
        # for i in want:
        #     want_mas.append(dd[i])

        date_list = [datetime.strptime(dd['DATE'][j], '%Y%m%d') for j in range(len(dd['DATE']))]
        # plt.plot(date_list,want_mas[0])
        # plt.show()
        # print(date_list)
        # print(want_mas)
        # for el in data_list:
        #     for names in el:
        #         nam=re.sub(r'[<> ]', '',names)
        #         dm[nam]=el.index(names)
        #     break

        # file.seek(0)
        # next(data)
        # l_d = list(data)
        #
        # for want_el in want:
        #     if want_el.upper() in dm:
        #         indexx =dm[want_el.upper()]
        #     else:
        #         print('ffffffff')
        # choosen_data = []
        # date_list = []
        #
        # # print(dm['DATE'])
        #
        # for i in list(l_d):
        #     # print(list(data))
        #     choosen_data.append(float(i[indexx]))
        #     # date_list.append(datetime.strptime(i[dm['DATE']], '%Y%m%d'))

    return [date_list,want_mas]
def vvod(prod='y'):
    n=0

    l_w=[]

    while (prod == 'y') and n<4:
        n += 1
        dopustim_data = "open/close/high/low"
        try:
            wanted = input("Введите желаемые данные open/close/high/low: ")
            if wanted not in dopustim_data:
                raise ValueError
            else:
                l_w.append(wanted.upper())  # здесь названия графиков
        except ValueError as err:
            print(err)
            n -= 1
            print('допустимые для получения данные: ', dopustim_data)

        prod = input("Продолжаем y/n?")

        # if n==4:

        # w, vr = open_file('APTK1.csv', l_w)
        # print(w)
        # print(vr)
    return [l_w,open_file('APTK1.csv', l_w)]
def create_plot(x_d,y_d, names):
    colors=['c','y','m','k']
    if len(y_d)==1:
        # plt.figure(figsize=(12, 6))
        plt.plot(x_d, y_d[0], color='g', marker='o', markersize=5)
        plt.xlabel('Дата')
        # plt.grid()
        plt.ylabel(f'{names[0]}')
       # / plt.bar(x_d,y_d[0], linewidth=1.0, edgecolor='k', width=0.1)


    else:
        fig,axs=plt.subplots(len(y_znach_mas))
        # axs.set_xlabel('Дата')
        for i in range(len(y_d)):
            axs[i].plot(x_d,y_znach_mas[i],label=f'{names[i]}',marker='o',markersize=5,color=colors[i])
            axs[i].set_xlabel('Дата')
            axs[i].set_ylabel(f'{names[i]}, $')
            plt.tight_layout()
        return plt.show()





data_for_plot=vvod()

names_plot,x_y=data_for_plot
x_date,y_znach_mas=x_y


create_plot(x_date,y_znach_mas,names_plot)

# print(data_for_plot[0])
# print(data_for_plot[1])
# data_x=data_for_plot[1][0]
# y_s=data_for_plot[1][1]
# # print(data_for_plot[1][1][0])
# # print(data_for_plot[1][1][1])

# y,x=open_file('APTK1.csv',wanted)
# fig,axs=plt.subplots(3,figsize=(8,4))
# axs[0].plot(x, y, label='Цена закрытия', color='g', marker='o', markersize=5)
# axs[0].set_xlabel('Дата')
# axs[0].set_ylabel('Цена закрытия, $')
#
# axs[1].bar(x,y, label='Цена закрытия', alpha=0.5,width=5,linewidth=0.7)
# axs[1].set_xlabel('Дата')
# axs[1].set_ylabel('Цена закрытия, $')
# plt.show()
# print(y)
# array_data,name_of_data=open_file(f'APTK1.csv')
#
# def get_data(a_d,indexx):
#     choosen_data=[]
#     for i in a_d:
#         choosen_data.append(float(i[indexx]))
#     return choosen_data
# if wanted.upper() in name_of_data:
#     indexx=name_of_data[wanted.upper()]
#     print(get_data(array_data,indexx))

    # date_list=[datetime.strptime(elem[date_index], '%Y%m%d') for elem in data]
    # close_list=[float(elem[close_index]) for elem in data]

    # for elem in data:
    #     # print(elem)
    #     date_fmt=datetime.strptime(elem[date_index], '%Y%m%d')
    #     date_list.append(date_fmt)
    #     close_list.append(float(elem[close_index]))
    #     high_list.append(float(elem[high_index]))



# date_list=date_list[10:15]
# close_list=close_list[10:15]


# plt.figure(figsize=(12, 6))
# plt.plot(date_list, close_list, label='Цена закрытия', color='g', marker='o', markersize=5)
# plt.bar(date_list, close_list, label='Цена MAX', alpha=0.5,width=5,linewidth=0.7)
# # plt.hist(close_list,bins=len(close_list),edgecolor='white')
# plt.title(f'График изменения цены акции Аптеки36и6')
# plt.xlabel('Дата')
# plt.ylabel('Цена закрытия, $')
# plt.legend()
# plt.show()



