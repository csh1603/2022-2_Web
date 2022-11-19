#2171081 조승현
import zipfile
#프로세스바(진행상황)를 출력함
from tqdm import tqdm

#wordlist에 사용자가 입력한 dictionary 파일 이름 저장
wordlist = input("Enter wordlist file: ")
#zip_file에 사용자가 입력한 crack을 위한 zip 파일 이름 저장
zip_file = input("Enter zip file: ")

#zip 파일을 읽고 쓰는 클래스, extractall() 사용을 위해 실행
zip_file = zipfile.ZipFile(zip_file)
#dictionary 파일에 있는 단어의 개수를 저장하여 n_words에 저장
n_words = len(list(open(wordlist, "rb")))

#wordlist 파일을 열고 닫음
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total = n_words, unit = "word"):
        try:
            #extractall이 password가 맞지 않으면 오류를 일으키기에 try문에서 실행
            zip_file.extractall(pwd=word.strip())
        except:
            #dictionary에서 읽어낸 password가 아니라면 (위의 try문에서 오류 발생), 계속 실행
            continue
        else:
            #dictionary에서 읽어낸 password가 zipfile의 패스워드라면 아래의 명령문 실행
            print("Password found:", word.decode().strip())
            #아래의 명령문 실행하지 않고 종료
            exit(0)
print("Password not found, try other wordlist.") 
