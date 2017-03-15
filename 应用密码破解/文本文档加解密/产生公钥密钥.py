#-*-coding:utf-8-*-
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64

# α�����������
random_generator = Random.new().read
# rsa�㷨����ʵ��
rsa = RSA.generate(1024, random_generator)
 
# master����Կ�Ե�����
#private_pem = rsa.exportKey()
 
#with open('master-private.pem', 'w') as f:
#  f.write(private_pem)
 
#public_pem = rsa.publickey().exportKey()
#with open('master-public.pem', 'w') as f:
#f   f.write(public_pem)
 
# ghost����Կ�Ե�����
private_pem = rsa.exportKey()
with open('ghost-private.pem', 'w') as f:
  f.write(private_pem)
 
public_pem = rsa.publickey().exportKey()
with open('ghost-public.pem', 'w') as f:
  f.write(public_pem)