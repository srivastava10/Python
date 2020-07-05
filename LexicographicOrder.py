x = int(input())
y = int(input())
z = int(input())
n = int(input())
i=0
j=0
k=0
print [ [ i, j,k] for i in range( x + 1) and for j in range( y + 1) and for k in range(z+1) if ( ( i + j + k ) != n )]
