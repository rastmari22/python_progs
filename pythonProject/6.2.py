# import random
#
#
# class Counter:
#     # name=''
#     # count=0
#     def __init__(self,name='',count=0):
#         self.name=name
#         self.count=count
#     def __isub__(self, other):
#         self.count-=other
#     def __iadd__(self,other):
#         self.count+=other
#         return self
#     def __str__(self):
#         if self.name=='pos':
#             return f"Положительные числа: {self.count}"
#         if self.name=='neg':
#             return f"Отрицательные числа: {self.count}"
#         return f"{self.name} состояние: {self.count}"
# def generate_random_numbers(count,min_val, max_val):
#     for _ in range(count):
#         yield random.randint(min_val, max_val)
# def main():
#     positive_counter=Counter('pos')
#     negative_counter=Counter('neg')
#
#     vib=int(input('Введите размер выборки: '))
#     min_val=-vib
#     max_val=vib
#     g=[random.randint(min_val, max_val) for x in range(vib)]
#     for i in g:
#         if i>0:
#             positive_counter+=1
#         elif i<0:
#             negative_counter+=1
#     print(positive_counter)
#     print(negative_counter)
#
# main()
import random


class Counter:
    # name=''
    # count=0
    def __init__(self,name='',count=0):
        self.__name=name
        self.__count=count

    @property
    def count(self):
        return self.__count
    @count.setter
    def count(self, count):
        self.__count=count
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name
    # @staticmethod
    # def __check_name(name):
    #     if isinstance(name, str):
    #         if name is not ('neg' or 'pos'):
    #             raise ValueError
    #         return name
    #     else:
    #         raise ValueError

    def __isub__(self, other):
        self.count-=other
    def __iadd__(self,other):
        self.count+=other
        return self
    def __str__(self):
        if self.name=='pos':
            return f"Положительные числа: {self.count}"
        if self.name=='neg':
            return f"Отрицательные числа: {self.count}"
        # return f"{self.name} состояние: {self.count}"
def generate_random_numbers(count):
    i=0
    while i<count:
        yield random.randint(-100,100)
        i+=1

def main():
    positive_counter = Counter()
    negative_counter = Counter()

    positive_counter.name='pos'
    negative_counter.name='neg'

    print(positive_counter)
    print(negative_counter)

    size_of_sample=int(input('Введите размер выборки: '))

    for item in generate_random_numbers(size_of_sample):
        if item > 0:
            positive_counter += 1
        elif item < 0:
            negative_counter += 1

    print(positive_counter)
    print(negative_counter)
main()