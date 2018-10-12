import zipfile
import threading
flag =True
password_path='/root/txt/p1.txt'
zip_path='/root/txt/Joker.zip'
file_p=open(password_path,'r')
file_password=file_p.readlines()
file_zip=zipfile.ZipFile(zip_path)
def checkpassword(file_zip,file_password):
    try:
        file_zip.extractall(pwd=file_password)
        print("[+]passsword Found:"+file_password)
        flag=False
    except Exception as e:
        pass
for i in file_password:
    file_password = i.strip('\n')
    mythred=checkpassword(file_zip,file_password)
    if flag:
        mythread.start()
        print(mythread.getName(),"Start")
    else:
        break
