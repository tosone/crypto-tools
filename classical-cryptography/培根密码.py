#!/usr/bin/env python
#-*-coding:utf-8-*-
# 培根密码
###################################################################################################


def bacon():
    list1 = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa', 'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab', 'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba', 'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb', 'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa', 'Z': 'bbaab'}
    list2 = {'aaaaa': 'A', 'aaaab': 'B', 'aaaba': 'C', 'aaabb': 'D', 'aabaa': 'E', 'aabab': 'F', 'aabba': 'G', 'aabbb': 'H', 'abaaa': 'I', 'abaab': 'J', 'ababa': 'K', 'ababb': 'L', 'abbaa': 'M', 'abbab': 'N', 'abbba': 'O', 'abbbb': 'P', 'baaaa': 'Q', 'baaab': 'R', 'baaba': 'S', 'baabb': 'T', 'babaa': 'U', 'babab': 'V', 'babba': 'W', 'babbb': 'X', 'bbaaa': 'Y', 'bbaab': 'Z'}
    list3 = {'a': 'AAAAA', 'b': 'AAAAB', 'c': 'AAABA', 'd': 'AAABB', 'e': 'AABAA', 'f': 'AABAB', 'g': 'AABBA', 'h': 'AABBB', 'i': 'ABAAA', 'j': 'ABAAA', 'k': 'ABAAB', 'l': 'ABABA', 'm': 'ABABB', 'n': 'ABBAA', 'o': 'ABBAB', 'p': 'ABBBA', 'q': 'ABBBB', 'r': 'BAAAA', 's': 'BAAAB', 't': 'BAABA', 'u': 'BAABB', 'v': 'BAABB', 'w': 'BABAA', 'x': 'BABAB', 'y': 'BABBA', 'z': 'BABBB'}
    list4 = {'AAAAA': 'a', 'AAAAB': 'b', 'AAABA': 'c', 'AAABB': 'd', 'AABAA': 'e', 'AABAB': 'f', 'AABBA': 'g', 'AABBB': 'h', 'ABAAA': 'i', 'ABAAA': 'j', 'ABAAB': 'k', 'ABABA': 'l', 'ABABB': 'm', 'ABBAA': 'n', 'ABBAB': 'o', 'ABBBA': 'p', 'ABBBB': 'q', 'BAAAA': 'r', 'BAAAB': 's', 'BAABA': 't', 'BAABB': 'u', 'BAABB': 'v', 'BABAA': 'w', 'BABAB': 'x', 'BABBA': 'y', 'BABBB': 'z'}
    l4 = ''
    l2 = ''
    print('1.加密\n2.解密\n3.退出\n')
    select = int(raw_input('请选择：'))
    jia = ""
    if select == 1:
        input1 = raw_input('请您输入要加密的字符串:')
        print "加密后为:",
        if input1[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            for i1 in input1:
                print list1[i1],
            print ''
        else:
            for i3 in input1:
                print list3[i3],
            print ''
    elif select == 2:
        input4 = raw_input('输入密文，注;中间用空格隔开:')
        f_input = input4.split()
        print "解密后的为:",
        if f_input[0] in list4:
            for i4 in f_input:
                if i4 in list4:
                    l4 = l4 + list4[i4]
                else:
                    print "%s 不是培根密文" % i4
            print l4
        else:
            for i2 in f_input:
                if i2 in list2:
                    l2 = l2 + list2[i2]
                else:
                    print "%s 不是培根密文" % i2
            print l2
    else:
        import os
        os.system('cls')
        return
###################################################################################################

bacon()
