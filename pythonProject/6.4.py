# class Stack:
#     def __init__(self):
#         self.__stack=[]
#     @property
#     def stack(self):
#         return self.__stack
#     @stack.setter
#     def stack(self,st):
#         self.__stack.append(st)
#     @stack.getter
#     def stack(self):
#         return self.__stack
#     def __str__(self):
#         return self.__stack
#     def push(self,element):
#
#         self.stack.append(element)
#         print(f"{len(self.stack)}: {element}")
#     def pop(self):
#         try:
#             element=self.stack.pop()
#
#             print (f"{len(self.stack)+1}: {element}")
#             return
#         except IndexError:
#             print( f'Ошибка! Стек пуст')
#             return
#
#
#     def __str__(self):
#         print(len(self.stack))
#
# s=Stack()
# print('Помещаем в стек..')
# s.push(1)
# s.push(2)
# s.pop()
# s.push(3)
# print("Извлекаем из стека: ")
#
# s.pop()
# s.pop()
# # print(s)
# s.pop()
# s.pop()
from Dist import Dist
class Stack:
    def __init__(self):
        self.__stack=[]
    @property
    def stack(self):
        return self.__stack
    # @stack.setter
    # def stack(self,st):
    #     self.__stack.append(st)
    # @stack.getter
    # def stack(self):
    #     return self.__stack


    def __str__(self):
        stack_to_print = "Данные в стеке: "
        if not self.__check_is_empty():
            stack_to_print +=", ".join(str(i) for i in self.stack)
            return f"{stack_to_print}"
        else:
            return f"{stack_to_print}отсутсвуют "
    def push(self,element):
        self.stack.append(element)
        print(f"{len(self.stack)}: {element}")
    def pop(self):
        try:
            element=self.stack.pop()
            print (f"{len(self.stack)+1}: {element}")
            return
        except IndexError:
            print( f'Ошибка! Стек пуст')
            return

    def __check_is_empty(self):
        return len(self.stack)==0




d1=Dist(10,15.4)
d2=Dist(4,12.3)
d3=Dist(34,18)
dist_stack=Stack()
# dist_stack(d3)
print('Помещаем в стек..')
dist_stack.push(d1)
dist_stack.push(d2)
dist_stack.push(d3)
print("Извлекаем из стека: ")
dist_stack.pop()

print(dist_stack)
s=Stack()
print('Помещаем в стек..')
s.push(1)
s.push(2)

print(s)
s.push(3)
print("Извлекаем из стека: ")
s.pop()
s.pop()
s.pop()
s.pop()
print(s)
