#!/usr/bin/env python
#-*-coding:utf-8-*-


class Caesar():

    def __init__(self):
        super(Caesar, self).__init__()

    def select(self):
        print("凯撒密码\n")
        print("1.带字符\n2.不带字符\n3.退出\n")
        prefer = input("请输入你的选择：")
        try:
            select = int(prefer)
        except Exception as e:
            select = 3
        cipherText = input("输入密文：\n")
        if select == 1:
            self.withCharacter(cipherText)
        elif select == 2:
            self.withoutCharacter(cipherText)
        else:
            exit(0)

    def withCharacter(self, cipherText):
        for p in range(127):
            str1 = ''
            for char in cipherText:
                temp = chr((ord(char) + p) % 127)
                if 32 < ord(temp) < 127:
                    str1 = str1 + temp
                    feel = 1
                else:
                    feel = 0
                    break
            if feel == 1:
                print(str1)

    def withoutCharacter(self, cipherText):
        pass

if __name__ == "__main__":
    caesar = Caesar()
    caesar.select()
