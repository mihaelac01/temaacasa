"punctul1"
def suma(a,b):
    s=a+b
    return print("Suma numerelor ",a," si ",b," = ",s)


"punctul2"
def produsul(a,b):
    p=a*b
    return print(" Produsul numerelor ",a," si ",b," = ",p)


"punctul3"
def media(a,b):
    n=(a+b)/2
    return print(" Media aritmetica a numerelor ",a," si ",b," = ",n)


"punctul4"
def celmaimaredivizor(a,b):
    t=[]
    u=[]
    for i in range (1,a+1):
        if (a%i==0):
            t.append(i)
    for j in range (1,b+1):
        if (b%j==0):
            u.append(j)
    c=set(t).intersection(u)
    g=max(c)
    return print(" Cel mai mare divizor comun al numerelor ",a," si ",b," = ",g)

"punctul5"
def celmaimicmultipluc(a,b):
    if a>b:
        mlt=a
    elif b>a:
        mlt=b
    else:
        mlt=a
    while True:
        if ((mlt%a==0)and(mlt%b==0)):
            cm=mlt
            break
        mlt +=1
    return print("Cel mai mic multiplu comun al numerelor ",a," si ",b," = ",cm)


"punctul6"
def nrmin(a,b):
    if a<b:
        return print(" Numarul minim =",a)
    else:
        return print(" Numarul minim =",b)


"punctul7"
def nrmax(a,b):
    if a>b:
        return print("Numarul maxim = ",a)
    else:
        return print("Numarul maxim =",b)


"punctul8"
def suma2():
    a= int(input('Dati primul numar: '))
    b= int(input('Dati al doilea numar: '))
    c=a+b
    return print("suma= ",a," + ",b," = ",c)


"punctul9"
def produs2():
    a= int(input('Dati un nr='))
    b= int(input('Dati al doilea nr='))
    c=a*b
    return print(" produs= ",a," x ",b," = ",c)
    

"punctul10"
def div(a,b):
    m=[]
    l=[]
    for i in range (1,a+1):
        if (a%i==0):
            m.append(i)
    for j in range (1,b+1):
        if (b%j==0):
            l.append(j)
    c=set(m).intersection(l)
    br=list(c)
    return print("divizorii comuni ai numerelor ",a," si ",b," = ",br)

"punctul11"
def cincimlt(a,b):
    c=[]
    if a>b:
        mlt=a
    elif b>a:
        mlt=b
    else:
        multiplu=a
    while len(c)<5:
        if ((mlt%a==0)and(mlt%b==0)):
            c.append(mlt)
            mlt +=1
        else:
            mlt+=1
    return print("5 multipli comuni ale numerelor ",a," si ",b," sunt=",c)


"punctul12"
def divizorcom(a,b):
    g=[]
    t=[]
    for i in str(a):
        g.append(int(i))
    for n in str(b):
        t.append(int(n))
    c=set(g).intersection(t)
    r=list(c)
    if len(r)!=0:
        return print("Cifrele comune  din numerele ",a," si ",b," sunt= ",r)
    else:
        return print(" nu au cifre comune")


"punctul13"
def cifrediferite(a,b):
    h=[]
    s=[]
    for i in str(a):
        h.append(int(i))
    for n in str(b):
        s.append(int(n))
    c=set(h).difference(s)
    x=list(c)
    return print("cifrele care se contin in numarul ",a," si nu se contin in numarul ",b," = ",x)

"punctul14"
def acelasindiv(a,b):
    z1=[]
    z2=[]
    for i in range (1,a+1):
        if (a%i==0):
            z1.append(i)
    for n in range (1,b+1):
        if (b%n==0):
            z2.append(n)
    if len(z1)==len(z2):
        return print("nr sunt PRIETENE")
    else:
        return print("nr nu sunt PRIETENE") 


nr1= int(input('dati nr1='))
nr2= int(input('dati nr2='))
#1)
suma(nr1,nr2)
#2)
produsul(nr1,nr2)
#3)
media(nr1,nr2)
#4)
celmaimaredivizor(nr1,nr2)
#5)
celmaimicmultipluc(nr1,nr2)
#6)
nrmin(nr1,nr2)
#7)
nrmax(nr1,nr2)
#10)
div(nr1,nr2)
#11)
cincimlt(nr1,nr2)
#12)
divizorcom(nr1,nr2)
#13)
cifrediferite(nr1,nr2)
#14)
acelasindiv(nr1,nr2)
#8)
suma2()
#9)
produs2()