import cmath
# Enter your code here. Read input from STDIN. Print output to STDOUT
def complex_to_polar():
    z = complex(input())
    print(abs(z))
    print(cmath.phase(z))
    
complex_to_polar()
    