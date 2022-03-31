#Chapter02-1
#파이썬 완전 기초
#Print 사용


#기본출력
print('Python start!')
print("Python start!")
print('''Python start!''')
print("""Python start!""")

print()

#separator 옵션
print('P','Y','T','H','O','N', sep= '')
print('010','7777','1234',sep='-')
print('python','google.com', sep='@')

#end 옵션

print('welcome to',end=' ')
print('IT News',end=' ')
print('Web Site')

#file option
import sys

print('Learn Python',file=sys.stdout)
print()

#format 사용(d : 3, s : 'python', f : 3.1445454)
print('%s %s' % ('one','two'))
print('{0} {1}'.format('one','two'))
print('{1} {0}'.format('one','two'))

print()


# %s
print('%10s' % ('nice'))
print ('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:$>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))
print('%5s' % ('pythonstudy'))
print('{10.5}'.format('pythonstudy'))


# %d
print('%d %d' & (1,2))
