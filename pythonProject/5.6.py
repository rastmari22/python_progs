def decoFunc(f):
    ps=111
    def ff(args):
        if args==ps:
            print('доступ к функции открыт!')
            return f(args)
        else:
            print("Доступ закрыт")
    return ff
@decoFunc
def func(pswd):
    if input('Вы ввели верный пароль. Поздоровайтесь: ') =='hi' :
        print('Goodbye!')
    else:
        print("(((")


n=int(input('Введите пароль '))

func(n)