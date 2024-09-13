n=int(input())
for i in range(1,n+1):
    space = " " * (n-i)
    if i==1:
        row = space + "* "
        print(row)
    elif i==n:
        print("* " * n)
    else:
        hollow = "  " * (i-2)
        row = space + "* " + hollow + "*"
        print(row)