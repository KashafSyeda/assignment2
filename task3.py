''' OUTPUT
1
1 2
1 2 3
1 2 3 4'''


print("task 3")
n = int(input("enter number of rows: "))
for i in range (1,n+1):
    print("\r")
    for j in range(0, i):
             print(j+1, end=" ")
