in=int(input())
if in>1:
    for i in range(2,in):
        if in%i==0:
            print("no")
            break
    else:
        print("yes")
else:
    print("no")
