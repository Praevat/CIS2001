import Lab2ProgressionClass
r = float(input("Please input a number less than 1")
while r >=1 or r is str() :
    r = float(input("Please input a number less than 1")

 g_prog = Lab2ProgressionClass.GeometricProgression(r)
 dividend = 1 - r
 expected = 1/dividend
 g_next = next(g_prog)
print (expected) # prints expected output

while abs(expected-g_next) > 0.000001 # stops when expected difference is close enough
    print(g_next)
    g_next += next(g_prog)