# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

ab = int(input())
bc = int(input())
ac = (ab**2 + bc**2)**.5
mc = ac/2

m_to_mid_bc = (mc**2 - (bc/2)**2)**.5
theta = round(math.atan(m_to_mid_bc/(bc/2))*180/math.pi)
print(str(theta) + u"\N{DEGREE SIGN}")
#tangent
# find angle of C, sohcahtoa
