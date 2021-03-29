a=int(input())  #4
b=int(input())  #6

for i in range(b, a*b+1):
    if i % a==0 and i % b==0:
        kmm= i
        break

print(kmm)

