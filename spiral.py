num= int(input('enter the number:'))
k=[[i for i in range(num)] for j in range(num)]
n=1
left=0
right=num-1
count=int((num+1)/2)
for i in range(count):
    for j in range(left,right+1):
        k[i][j]=n
        n=n+1
    for j in range(left+1,right+1):
        k[j][right]=n
        n=n+1
    for j in range(right-1,left-1,-1):
        k[right][j]=n
        n=n+1
    for j in range(right-1,left,-1):
        k[j][left]=n
        n=n+1
        
    left=left+1
    right=right-1
        
for i in range(num):
    for j in range(num):
        print(k[i][j],end='\t')
    print(' ')
#print(k)
