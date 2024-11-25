import random 
n=int(input())
lista=[]
lista3d=[[0]*n,[0]*n,[0]*n]

for i in range(n):
    lista3d[0][i]=random.randint(1,1000)
    lista3d[1][i]=random.randint(1,1000)
    lista3d[2][i]=random.randint(1,1000)

print(lista3d)