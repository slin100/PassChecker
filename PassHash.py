import sys, hashlib, os, time as t
from time import time

def logo(long):
    print("          _________    ___         ___     __          ___"); t.sleep(long)
    print("         /  ______/   /  /        /__/    /  \        /  /"); t.sleep(long)
    print("        /  /         /  /        ___     /    \      /  / "); t.sleep(long)
    print("       /  /____     /  /        /  /    /  /\  \    /  /  "); t.sleep(long)
    print("      /____   /    /  /        /  /    /  /  \  \  /  /   "); t.sleep(long)
    print("          /  /    /  /        /  /    /  /    \  \/  /    "); t.sleep(long)
    print("     ____/  /    /  /____    /  /    /  /      \    /     "); t.sleep(long)
    print("    /______/    /_______/   /__/    /__/        \__/      "); t.sleep(long)
logo(0.4)

try: pwd = sys.argv[1]
except: pwd = input(f"{os.getlogin()} enter the pasword to scan.\n")
try: database = sys.argv[2]
except: database = input(f"Enter the path to the database.\n")
message_digest = hashlib.sha1()
message_digest.update(bytes(pwd, encoding='utf-8'))
to_check = message_digest.hexdigest().upper()
start = time()
timePerSec=0
timePerSek=time()
leaked = False
with open(database) as file:
    num = 6135842; numPlus = 613584; count = 0; counter=0; counterPlus=0; timePerSecOld=555555555555555555555; oldTime=time()
    for line in file:
        if str(to_check) in str(line):
            print(f'\n\nYour password had been {line.split(":")[1].strip()} times leaked!')
            leaked = True
            break
        if count>=numPlus:
            s = f"Scan progress {counter}.{counterPlus}% Only {int(timePerSecOld/60)} minutes and {timePerSecOld%60} seconds left                            "
            print(s, end='')
            print('\r', end='')
            if count>=num:
                counter+=1
                num+=6135842
            else:
                timePerSec = time()
                timePerSec = timePerSec-timePerSek
                timePerSec = timePerSec*(1000-int(str(counter)+str(counterPlus)))
                timePerSec = int(timePerSec) 
                if timePerSec < timePerSecOld: timePerSecOld = timePerSec
                elif time()-oldTime > 1 and int(timePerSecOld)>=1:
                    timePerSecOld -=1
                    oldTime=time()
                timePerSek=time()
                counterPlus+=1
                if counterPlus==10: counterPlus=0
                numPlus+=613584
        count+=1
    if not leaked:
        end = time()
        print('\n\nYour password wase´t leaked in this database :)')
print(f"Scan finished in {int((end-start)/60)} minutes and {(end-start)%60} seconds")