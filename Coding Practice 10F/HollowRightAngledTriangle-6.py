n = int(input())
for i in range(n):
    space = "  " * i
    if i == 0:
        print("* " * n)
    elif i == (n-1):
        print(space + "*")
    else:
        hollow = "  " * (n-i-2)
        row = space + "* " + hollow +"* "
        print(row)