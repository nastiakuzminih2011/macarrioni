N = int(input())
M = int(input())
x = int(input())
y = int(input())
if M < N:
    N, M = M, N
a = N - x
b = M - y
if x >= a and y >= b:
   if a >= b:
	   print(b)
   else:
	   print(a)
elif x >= a and y <= b:
   if y >= a:
	   print(a)
   else:
	   print(y)
elif x <= a and y >= b:
   if x >= b:
	   print(b)
   else:
	   print(x)
elif x <= a and y <= b:
   if x >= y:
	   print(y)
   else:
	   print(x)
