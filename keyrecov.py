from base64 import b64encode
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

#encrypt.py에서 공개키를 이용해 암호화한 대칭키를 다시 복호화
#대칭키를 암호화하고 저장한 파일 key.bin 읽기
file_in = open("key.bin", "rb")
#개인키를 이용하여 대칭키를 복호화함
private_key = RSA.import_key(open("private.pem").read())
enc_data = file_in.read(private_key.size_in_bytes())
cipher_rsa = PKCS1_OAEP.new(private_key)
#복호화한 데이터(대칭키)를 data에 저장하고 base64 encoding 진행
data = cipher_rsa.decrypt(enc_data)
data = b64encode(data)
#위에서 계산한 결과를 "key.txt"에 저장
file_out = open("key.txt", "wb")
file_out.write(data)
file_in.close()
file_out.close()
