#-*-coding:utf-8-*-
import base64
import os

from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5

# 伪随机数生成器
random_generator = Random.new().read
# rsa算法生成实例
rsa = RSA.generate(1024, random_generator)

print u"请把你要解密的文件放到此文件的同级目录"
print u"请输入要解密的文件名：",
ciphertext = raw_input()

if os.path.exists('ghost-private.pem'):
    dd = open(ciphertext)
    for line in dd.read().split('\n'):
        with open('ghost-private.pem') as f:
            key = f.read()
            rsakey = RSA.importKey(key)
            cipher = Cipher_pkcs1_v1_5.new(rsakey)
            try:
                text = cipher.decrypt(base64.b64decode(line), random_generator)
            except ValueError:
                pass
            text = text.replace('rnxxx', '\r\n').replace('rxxx', '\r').replace('nxxx', '\n')
            ff = open('Plaintext.txt', 'a')
            ff.write(text)
    print u"解密成功!明文为:Plaintext.txt"
    print u"按enter键结束..."
    raw_input("")
    dd.close()
    ff.close()
else:
    print u"请把你的私钥放到此文件的同级目录"
