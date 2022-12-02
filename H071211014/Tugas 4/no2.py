x = int(input())
y = int(input())   

def getFPB(x, y):
   while(y):
       x, y = y, (x % y)
   return x

print('FPB dari', x,'dan', y,'=', getFPB(x, y))