# programme principal
print ("Hello World")
choix=input("choisissez 1 pour base10 vers base16 ou 2 pour base16 vers base10: ")
def dec(a): 
    if a<=9:
        return a
    
    if a==10:
        a='A'
    elif a==11:
        a='B'
    elif a==12:
        a='C'
    elif a==13:
        a='D'
    elif a==14:
        a='E'
    elif a==15:
        a='F'
    return a

if str(choix)=="1":
    a=int(input("entrez un nombre en decimal(base10): "))
    n=a #précedement "a" a été définie par int() donc on doit présenté une autre variable qui est considéré comme une valeur.
    ch=''
    while a<=15:
        print(dec(a))
        break #break permet d'interrompre une boucle.
    while a>=16:
        i=n%16 #i est le reste de la division euclédienne de n par 16.
        if n<16:
            ch=ch+str(dec(i)) #on rajoute un terme à la chaine de caractère.
            break
        else:
            ch=ch+str(dec(i))
        n=n//16 #ce calcule recommence tant que le nouveau n obtenu est superieur à 15.
    nch=""
    for x in reversed(ch): #pour inverser la chaine de caractère.
        nch=nch+str(x)
    print(nch)
#on a utilisé str() car on ne peut pas ajouté a un str un int().
if str(choix)=="2":
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
print(nch)

