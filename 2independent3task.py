import math 
x1=2 
y1=1 
answer1task=((x1**y1)**x1)+x1**x1**y1-x1**4 
print("1)",answer1task) 
 
 
x2 = 1 
y2 = 4 
z2 = 3 
answer2task = math.pow((abs(1 / math.tan(y2) + 6)), 1/3)+ math.sqrt((x2+1)**3/(4*y2-2*z2)) 
print("2)", answer2task) 
 
 
x3 = 3 
y3 = 0.2 
answer3task= 5*x3*y3/(x3**3-4) + math.exp(x3**2) + math.sqrt(math.cos(y3)**2-y3**2) 
print("3)", answer3task) 
 
 
x4 = 3 
y4 = 5 
answer4task = math.sqrt(abs(y4)) + math.atan(math.log10(x4)/math.log10(math.e))**3/(x4**y4-y4+1) 
print("4)", answer4task) 
 
x5 = 3 
y5 = 1 
z5 = 2 
answer5task = 4**(x5*y5) - x5**(y5*z5)+(x5*y5)**5 
print("5)", answer5task) 
 
x6 = 2 
y6 = 2 
z6 = 1 
answer6task = (4*abs(x6) - (x6*y6*z6)**2)/(x6 + math.exp(y6*x6) - 2*y6*z6) 
print("6)", answer6task) 
 
x7 = 0.8 
y7 = 0.1 
z7 = 4 
answer7task=math.sqrt((1-x7+math.atan(x7-7*y7))/(4*x7*z7-math.pow(math.log10(y7),2))) 
print('7)', answer7task) 
 
x8 = 3 
y8 = 1 
z8 = 3 
answer8task = 2*3*4/(math.sin(x8)**3 + math.tan(y8)**3) - math.sqrt(z8**(x8-y8)) 
print('8)', answer8task) 
 
 
x9 = 4 
answer9task = ((math.log10(x9-3)/math.log10(math.e))**4+2**x9*math.sin(3*x9)**2)/ (4 *x9 - 5.2) 
print('9)', answer9task) 
 
x10 = 2 
y10 = 2 
z10 = 1 
answer10 = math.sqrt(0.6*x10*y10*z10) + (y10**x10)**2 - math.exp(math.sin(2*x10**2)) 
print('10)', answer10) 
 
x11 = 0.5 
y11 = 2 
answer11 = math.asin(x11**3)-6/(8*(math.cos(4*y11) - math.sin(4*x11))) 
print('11)', answer11) 
 
x12 = 2 
y12 = 1 
z12 = 3 
answer12 = abs(math.log10(x12**3)/math.log10(math.e)) + math.exp(2*x12)/(x12+3.4) - 1 / math.tan(3/x12*y12*z12)**3 
print('12)', answer12)
