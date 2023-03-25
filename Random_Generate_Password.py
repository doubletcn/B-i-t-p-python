
#tạo mật khẩu ngẫu nhiên

import string
import random

letter=string.ascii_letters
number=string.digits
punctuation=string.punctuation

def rGPass(length=8):
    password=f'{letter}{number}{punctuation}'
    password=list(password)
    password=random.choices(password,k=length)
    password=''.join(password)
    return password

def passLength():
    pass_Length=input("please enter long of password: ")
    return int(pass_Length)

def main():
    pass_Length=passLength()
    Pass=rGPass(pass_Length)
    print(Pass)

if __name__=="__main__":
    main()