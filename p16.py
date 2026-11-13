import sys
sys.setrecursionlimit(10**6)
def double(n):
    print(n,' ',end="")
    if n == 1:
        return n
    else:
        return n + double(n-1)
def recur3():
    print('limit: ',sys.getrecursionlimit())
    ans = 'y'
    while(ans == 'y'):
        numb=int(input('enter a number -> '))
        a = double(numb)
        print(numb,'+','=',a)
        ans = input('Another number (y/n): ')
        print('-------')
recur3()