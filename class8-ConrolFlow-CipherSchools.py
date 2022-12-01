# 5 5 5 5 5
# 5 4 4 4 5
# 5 4 3 4 5
# 5 4 4 4 5
# 5 5 5 5 5
n=5
for i in range(n):
    for j in range(n):
        print(max(i+1,j+1,n-i,n-j),end=" ")
    print()