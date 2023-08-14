def zarb(n,m):
    for i in range (1,n+1):
        print ("\t")
        for j in range(1,m+1):
            print(i*j,end='  ')

n= int (input("enter first number:"))
m= int (input("enter second number:"))
zarb(m,n)