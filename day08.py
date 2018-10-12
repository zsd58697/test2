'''
import crypt
def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open("/root/txt/dic.txt","r")
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word,salt)
        if cryptWord == cryptPass:
            print("[+] Found Password:"+word)
        else:
            print("[-]Password {} Not Found.".format(word))
def main():
    passFile=open("/root/txt/password.txt")
    for line in passFile.readlines():
        if ':' in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print("[*] Cracking Password For:"+user)
            testPass(cryptPass)
if __name__ == "__main__":
    main()
'''
'''
import itertools
path1='/root/txt/password.txt'
mylist=(''.join(x) for x in itertools.product("ABCDEFJHIGKLMNOPQRSTUVWXYZabcdegjhigklmnopqrstuvwxyz",repeat=7))
print(next(mylist))
file_save=open(path1,'a',encoding='utf-8')
while 1:
    try:
        file_save.write(next(mylist)+'\n')
    except Exception as e:
        print(e)
        break
    finally:
        print('over')
'''
'''
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
    except Exception as e:
        pass
for i in file_password:
    file_password = i.strip('\n')
    checkpassword(file_zip,file_password)
'''

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
















    
