import crypt
def testPass(cryptPass):
    salt=cryptPass[0:2]
    dictFile = open("/root/txt/dic2.txt","r")
    for word in dictFile.readlins():
        word =word.strip('\n')
        cryword = crypt.crypt(word,salt)
        if cryword == cryptPass:
            print("[+] Found Password :" +word)
        else:
            print("[-] Password {} Not Found.".format(word))
def main():
    passFile=open("/root/txt/p2.txt")
    for line in passFile.readlines():
        if ':' in line:
            user=line.split(':')[0]
            cryptPass=line.split(':')[1].strip(' ')
            print("[*] Cracking password For: "+user)
            testPass(cryptPass)
main()
