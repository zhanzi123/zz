for m in range(1,10):
    for n in range(1,m+1):
        print("%d*%d=%d"%(m,n,m*n),end=" ")
    print()

for m in range(1,10):
    for n in range(1,m+1):
        print("{}*{}={}".format(m,n,m*n),end=" ")
    print()