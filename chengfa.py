#!/usr/bin/env python3

print('*'*50)
i=1
while i<10:
    n=1
    while n<10:
        print('{:2d}*{}={:2d}'.format(i,n,i*n),end=' ')
        n=n+1
    print()
    i+=1

