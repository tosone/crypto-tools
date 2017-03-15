#-*-coding:utf-8-*-


# base32
###################################################################################################
def base32():
    print('1.加密\n2.解密\n3.退出\n')
    select = int(raw_input('请选择：'))
    if select == 1:
        import base64
        str = raw_input('输入要加密的base字符串：')
        print 'base64encod:', base64.b64encode(str)
        print 'base32encod:', base64.b32encode(str)
        print 'base16encod:', base64.b16encode(str)
        raw_input("请输入任意键继续")
    elif select == 2:
        strf = raw_input('输入要破解的base字符串：')
        import base64

        try:
            base64.b64decode(strf).decode('utf-8')
            print 'base64decod:', base64.b64decode(strf).decode('utf-8')
        except:
            pass
        try:
            base64.b32decode(strf).decode('utf-8')
            print 'base32decod:', base64.b32decode(strf).decode('utf-8')
        except:
            passs
        try:
            base64.b16decode(strf)
            print 'base16decod:', base64.b16decode(strf).decode('utf-8')
        except:
            pass
        raw_input("请输入任意键继续")
    else:
        import os
        os.system('cls')
        return
#############s######################################################################################

base32()
