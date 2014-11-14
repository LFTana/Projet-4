# programme principal
print ("Hello World")
def hexa(a):
    if str(a)<'10':
        a=str(a)
    elif str(a)=='A':
        a=10
    elif str(a)=='B':
        a=11
    elif str(a)=='C':
        a=12
    elif str(a)=='D':
        a=13
    elif str(a)=='E':
        a=14
    elif str(a)=='F':
        a=15
    return a


ch=input("Entrer un nombre en Hexadecimale")
n=0
i=len(ch)-1
nch=0
while n<len(ch):
    a=ch[n]
    nch=nch+int(hexa(a))*16**i
    n=n+1
    i=i-1
print(nch,hexa(a))

