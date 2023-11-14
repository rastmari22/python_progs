# def f3(x):
#     return x%3==0
# def f5(x):
#     return x%5==0
# def f15(x):
#     return x%15==0
#
#
# array=[i for i in range(100)]
#
# s=list(filter(f3,array))
# print(s)
#
# s1=list(filter(lambda x: x%5==0,array))
# print(s1)
#
#
from abc import ABC, abstractmethod

class NumberDivisor(ABC):
    @abstractmethod
    def check_division(self, number, divisor):
        pass

class MyNumberDivisor(NumberDivisor):
    # def __init__(self, numbers):
    #     self.numbers = numbers
    @staticmethod
    def check_division( number, divisor):
        return number%divisor==0
    #
    # @staticmethod
    # def check_division(number, divisor):
    #     if number % divisor == 0:
    #         return number
    # @staticmethod
    # def check_array_division(self,arr,divisor):
    #     d=dict()
    #     results = []
    #     for number in arr:
    #         r = self.check_division(number, divisor)
    #         if  not r is None:
    #             results.append(r)
    #     return results
    def check_array_division(self,arr,divisor):
        d=dict()
        results = []
        # for delitel in (divisor):
        #     divisor[delitel]=arr.copy()
        #     # p=list(filter(self.check_division,(divisor[delitel],3)))

            # dint=int(delitel)
        for number in arr:
            if  not self.check_division(number, divisor) is None:
                results.append(self.check_division(number, divisor))
        return results

#

arraay=[j for j in range(100)]

my_divisor = MyNumberDivisor()
dd={"15":[],"3":[],"5":[]}

# print(my_divisor.check_array_division(arraay,dd))
print(my_divisor.check_array_division(arraay,15))
print(my_divisor.check_array_division(arraay,3))
print(my_divisor.check_array_division(arraay,5))


class div:
    @staticmethod
    def is_3(num):
        if num%3==0:
            return f'делится на 3'
        pass
    @staticmethod
    def is_5(num):
        if num % 5 == 0:
            return f'делится на 5'
        return num
    @staticmethod
    def is_15(num):
        if num % 15 == 0:
            return f'делится на 15'
        pass
arraay=[j for j in range(100)]

d=div()

for i in arraay:
    print(d.is_15(i) or d.is_3(i) or d.is_5(i) )
