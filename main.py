from SupportFiles import registration
from SupportFiles import checkFace
from random import randint
from transliterate import translit
from os import system
from time import sleep

def start():
    while True:
        system('CLS')
        print('1-registration\n2-checkFace')
        a=input()
        if a=='1':
            try:
                id=randint(100000,1000000)
                first = translit(input("Имя: "), language_code='ru', reversed=True)
                sur = translit(input('Фамилия: '), language_code='ru', reversed=True)
                position = translit(input('Должность: '), language_code='ru', reversed=True)
                registration.register(id,first,sur,position)
            except:
                print('Ошибка регистрации')
        if a=='2':
            try:
                print(checkFace.check())
            except:
                print('Ошибка распознования лица')
        sleep(2)

if __name__=='__main__':
    start()