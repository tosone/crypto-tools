#-*-coding:utf-8-*-
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64
import os

# 伪随机数生成器
random_generator = Random.new().read
# rsa算法生成实例
rsa = RSA.generate(1024, random_generator)
 
# master的秘钥对的生成
#private_pem = rsa.exportKey()
 
#with open('master-private.pem', 'w') as f:
  #f.write(private_pem)
 
#public_pem = rsa.publickey().exportKey()
#with open('master-public.pem', 'w') as f:
#  f.write(public_pem)
 
# ghost的秘钥对的生成
#private_pem = rsa.exportKey()
#with open('ghost-private.pem', 'w') as f:
#  f.write(private_pem)
 
#public_pem = rsa.publickey().exportKey()
#with open('ghost-public.pem', 'w') as f:
#  f.write(public_pem)


print u"请把你要加密的文件放到此文件的同级目录"
print u"请输入要加密的文件名:",
qq= raw_input("")
dd=open(qq,'r')
fx = dd.read().replace('\r\n', 'rnxxx').replace('\r', 'rxxx').replace('\n', 'nxxx')
dd.close()
zz=open(qq,'w')
zz.write(fx)
zz.close()
zz=open(qq,'r')
fs=zz.read()
xx=open('Ciphertext.txt','a')
len=len(fs)
i=0
if os.path.exists('ghost-public.pem'):
   while (i*64)<len:
      zz.seek(64*i,0)
      message=zz.read(64) 
      i=i+1

 
      with open('ghost-public.pem') as f:
          key = f.read()
          rsakey = RSA.importKey(key)
          cipher = Cipher_pkcs1_v1_5.new(rsakey)
          cipher_text = base64.b64encode(cipher.encrypt(message))+"\n"
          #ff=open('xx.txt','a')
          xx.write(cipher_text)
          #print cipher_text
   print u"加密成功！密文为：Ciphertext.txt"
   print u"按enter键结束。"
   raw_input("")
else : print u"请生成公钥、私钥"     
dd.close()
xx.close()

