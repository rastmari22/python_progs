# def fib(n):
#     s=0
#     i = 1
#     s1 = 0
#     s2 = 0
#     while True:
#         if i==1:
#             s1=i
#             yield i
#             i+=1
#         if i==2:
#             s=s1+s2
#             yield s
#             i+=1
#         s2=s
#         s=s1+s2
#         s1=s2
#         i += 1
#         if s<=n: yield s
#

def fib(lim):
    s1,s2=0,1
    while s2<lim:
        yield s2
        s1,s2=s2, s1+s2


lim=int(input('Введите верхнюю границу: '))
print(f"Числа Фибоначчи в диапазоне от 1 до {lim}: ")

for i in fib(lim):
    print(i,end=' ')