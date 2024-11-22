import time
import os
k=0
x=1
y=0
t=0
w=False
n=int(input())
while True:
    if w:
        print(k)
    w=True
    if k<=10:
        x=1;y=7;t=7
    elif k<=15:
        x=7;y=3;t=7
    elif k<=25:
        x=7;y=7;t=2
    elif k<=30:
        x=7;y=3;t=7
    for i in range(n):
        for j in range(n):
            if i==0  or i==n-1:
                print('-',end='',flush=True)
            elif j==0 or j==n-1:
                print('|',end='')
            elif i<=n//3:
                print(f'\033[3{x}m*\033[0m',end='',flush=True)
            elif i<=(n//3)*2:
                print(f'\033[3{y}m*\033[0m',end='',flush=True)
            elif i<=n:
                print(f'\033[3{t}m*\033[0m',end='',flush=True)
            else:
                print(' ',end='',flush=True)
        print()
    time.sleep(1)
    k+=1
    os.system('cls' if os.name == 'nt' else 'clear')
    if k==30:
       k=0
       w=False