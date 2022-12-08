import os

from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

#encrypt.py에 지정해둔 iv 불러오기
iv = b64decode('CEco1lPPgNWtKkV91FDJdA==')
try:
	#현재 파이썬이 위치한 폴더 내에 있는 모든 파일 이름을 filename에 저장
	for filename in os.listdir():
		#만약 filename의 확장자를 분리했을 때 enc 파일이라면 아래의 명령 실행
		if os.path.splitext(filename)[1] == '.enc':
			s = os.path.splitext(filename)[0]
			with open(filename, "rb") as f:
				data = f.read()
				#keyrecov.py을 통해 생성한 key.txt를 base 64 decoding을 통해 다시 저장
				key = b64decode(open("key.txt", "rb").read())
				cipher = AES.new(key, AES.MODE_CBC, iv)
				pt = unpad(cipher.decrypt(data), AES.block_size)
				#다시 파일의 확장자를 txt로 변환하고 그 안에 원래 데이터 값을 써줌
				writeFile = open(s + '.txt', "wb")
				writeFile.write(pt)
				writeFile.close()
				# *.enc(암호화했던 파일)을 삭제
				os.remove(filename)
except ValueError:
	print("Incorrect decryption")
except KeyError:
	print("Incorrect Key")
