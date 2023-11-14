from abc import ABC,abstractmethod
class Divisible(ABC):
    @abstractmethod
    def is_div(self,num):
        pass
class DivBy15(Divisible):
    def is_div(self,num):
        return num%15==0
class DivBy3(Divisible):
    def is_div(self, num):
        return num % 3 == 0
class DivBy5(Divisible):
    def is_div(self, num):
        return num % 5 == 0

arraay=[j for j in range(100)]

divBy15=DivBy15()
divBy5=DivBy5()
divBy3=DivBy3()

for elem in arraay:
    if divBy15.is_div(elem):
        print(f"{elem} делится на 15")
    elif divBy3.is_div(elem):
        print(f"{elem} делится на 3")
    elif divBy5.is_div(elem):
        print(f"{elem} делится на 5")
    else:
        print(f"{elem} ")