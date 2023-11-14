from Dist import Dist
def test_dist(dist1, dist2):

    print(f'dist1 = {dist1}',
     f'dist2 = {dist2}',
     f'dist1 + dist2 = {dist1 + dist2}',
     f'dist1 - dist2 = {dist1 - dist2}',
     f'dist1 * dist2 = {dist1 * dist2}',
     f'dist1 / dist2 = {dist1 / dist2} ',
     f'dist1 == dist2 is {dist1 == dist2}',
     f'dist1 != dist2 is {dist1 != dist2}',
     f'dist1 < dist2 is {dist1 < dist2}',
     f'dist1 <= dist2 is {dist1 <= dist2}',
     f'dist1 > dist2 is {dist1 > dist2}',
     f'dist1 >= dist2 is {dist1 >= dist2}', sep='\n')



first_dist=Dist(12,35.)
second_dist=Dist(1,8.)

test_dist(first_dist,second_dist)
#


# from random import *
#
#
# class CRM:
#     def __init__(self):
#         self.__abiturients = {}
#
#     def add(self, abiturient):
#         # получение СНИЛСа
#         number = abiturient.get_number()
#
#         # добавление абитуриента в словарь,
#         # где информация хранится под СНИЛСами
#         if self.__is_number(number):
#             if number in self.__abiturients:
#                 raise ValueError("Абитуриент уже внесён в базу")
#             self.__abiturients[number] = abiturient
#         else:
#             raise ValueError("СНИЛС введён некорректно")
#
#     def get_status(self, number):
#         return self.__abiturients[number].get_status()
#
#     # проверка на корректность СНИЛСа
#     @staticmethod
#     def __is_number(number):
#         return number[0:3].isdigit() and number[3] == "-" and number[4:7].isdigit() and \
#             number[7] == "-" and number[8:11].isdigit() and number[11] == " " and number[12:].isdigit()
#
#
# class Abiturient:
#     def __init__(self, name, surname, patronymic, age, number, bvi=False):
#         self.__name = name
#         self.__surname = surname
#         self.__patronymic = patronymic
#         self.__age = age
#
#         # СНИЛС
#         self.__number = number
#
#         # Russian National Exam (ЕГЭ), баллы
#         self.__RNE = self.__fetch_RNE()
#
#         # есть ли БВИ
#         self.__bvi = bvi
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = self.__check_name(name)
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, surname):
#         self.__surname = self.__check_name(surname)
#
#     @property
#     def patronymic(self):
#         return self.__patronymic
#
#     @patronymic.setter
#     def patronymic(self, patronymic):
#         self.__patronymic = self.__check_name(patronymic)
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if isinstance(age, int):
#             self.__age = age
#         else:
#             raise ValueError
#
#     @property
#     def bvi(self):
#         return self.__bvi
#
#     @bvi.setter
#     def bvi(self, bvi):
#         if isinstance(bvi, bool):
#             self.__bvi = bvi
#         else:
#             raise ValueError
#
#     @property
#     def RNE(self):
#         return self.__RNE
#
#     # проверка, все ли результаты ЕГЭ корректны
#     @RNE.setter
#     def RNE(self, RNE):
#         if isinstance(RNE, tuple):
#             if len(RNE) != 3:
#                 raise ValueError
#             if any(x < 0 or x > 100 for x in RNE):
#                 raise ValueError
#             if all(isinstance(x, int) for x in RNE):
#                 self.__RNE = RNE
#             else:
#                 raise ValueError
#         else:
#             raise ValueError
#
#     # функция получения результатов ЕГЭ
#     def __fetch_RNE(self):
#         return (randint(0, 100) for _ in range(3))
#
#     # функция ответа на вопрос, проходит ли абитуриент
#     def __check(self):
#         if self.__bvi:
#             return "Да"
#         if random() > 0.95:
#             return "Да"
#         return "Нет"
#
#     # проверка, является ли имя именем
#     @staticmethod
#     def __check_name(name):
#         if isinstance(name, str):
#             if name.isalpha():
#                 raise ValueError
#             # первая буква должна быть большой
#             return name.capitalize()
#         else:
#             raise ValueError
#
#     def get_number(self):
#         return self.__number
#
#     def get_status(self):
#         return self.__check()
#
#
# module = CRM()
#
# # добавление АР-а в список абитуриентов
# module.add(Abiturient("fлександр", "Вотяков", "Романович", 18, "111-222-333 00", True))
#
# # добавление РА в список абитуриентов
# module.add(Abiturient("Роман", "Вотяков", "Александрович", 18, "333-222-111 00"))
#
# # проверка, проходят ли абитуриенты
# print(module.get_status("111-222-333 00"))
# print(module.get_status("333-222-111 00"))