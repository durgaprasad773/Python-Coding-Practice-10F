n=int(input())

for i in range(1,n+1):
    space = " " * (n-i)
    if i == 1:
        print(space + "* ")
    else:
        hollow = "  " * (i-2)
        row = space + "* " + hollow + "* "
        print(row)

for i in range(1,n):
    space = " " * i
    if i == (n-1):
        print(space + "*")
    else:
        hollow = "  " * (n-i-2)
        row = space + "* " + hollow + "* "
        print(row)