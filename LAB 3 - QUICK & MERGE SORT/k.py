x=12230*23459
print(x)

def karatsuba(x,y):
   if len(x) == 1 or len(y) == 1:
         return int(x)*int(y)
   n = len(x)
   mid = n//2
   XL, XR = x[:mid], x[mid:]
   YL, YR = y[:mid], y[mid:]
   p1 = karatsuba(XL,YL)
   p2 = karatsuba(XR,YR)
   p3 = karatsuba(XL+XR,YL+YR)
   return (10**n)*p1 + (10**mid)*(p3-p1-p2) + p2
x = "12230"
y = "23459"
print(karatsuba(x,y)) 