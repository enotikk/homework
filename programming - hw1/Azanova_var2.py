a=input('a=..?\n')
b=input('b=..?\n')
c=input('c=..?\n')
b=int(b)
if b<0:
    s=a+'x'+str(b)+'=0'
else:
    s=a+'x+'+str(b)+'=0'
a=int(a)
c=int(c)
if a*b==c:
    print('yes,',a,'*',b,'=',c)
else:
    print('no,',a,'*',b,'<>',c)
if a*c==-b:
    print('yes,',c,'is the root of',s)
else:
    print('no,',c,'is not the root of',s)