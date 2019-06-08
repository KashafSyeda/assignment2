print("numbers")
n = int(input("enter number of rows: "))
for i in range(1,n+1):
    print("\r")
    for j in range(0,i):
        print(i,end=" ")