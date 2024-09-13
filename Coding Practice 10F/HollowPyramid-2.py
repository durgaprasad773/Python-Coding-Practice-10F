n=int(input())
for i in range(1,n+1):
    if i == 1:
        print(str(i))
    else:
        hollow = "  " * (i-2)
        row = (str(i)+" ") + hollow + str(i)
        print(row)
  
num = n-1      
for i in range(1,n):
    if i == (n-1):
        print(str(num))
    else:
        hollow = "  " * (n-i-2)
        row = ((str(num) +" ")) + hollow + ((str(num)+" "))
        num = num - 1
        print(row)