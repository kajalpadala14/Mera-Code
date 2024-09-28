# n=int(input("Enter the len:"))
# i=0
# a=[]
# while i<n:
#     a.append(int(input()))
#     i+=1
# print(a)

# i=0
# while i<n:
#     print(a[i]**2 , end=" ")
#     i+=1
n = int(input())  
arr = list(map(int, input().split())) 
i = 0
while i < n:
    print(arr[i] ** 2, end=" ")  
    i += 1
