isp = []
zv = []
wrongs = 0
s_w=''
import random

words = ['av']
def add_wrongs():
    global wrongs
    wrongs+=1
    return wrongs
word = random.choice(words)
def to_isp(l):
    global isp
    isp.append(l)
def get_isp():
    global isp
    return isp
def isp_out():
    global isp
    return ", ".join(isp)

def gameover():
    global wrongs,s_w,word,zv
    m="".join(zv)
    if  "".join(zv)==word or s_w==word:
        print("Вы выиграли! Это слово: ", "".join(zv))
        return True
    if wrongs==8:
        print("Вы проиграли! Загаданное слово было: ", (word))
        return True
    else:
        return False
def start_word():
    global zv
    zv=[]
    for b in word:
        if b in isp:
            zv.append(b)
        else:
            zv.append('*')
    zw="".join(zv)
    # if zw== word:
    #     gameover()
    return zw
