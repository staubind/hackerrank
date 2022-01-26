# Enter your code here. Read input from STDIN. Print output to STDOUT


def polynomial_evaluation(poly,num, val):
    to_evaluate = poly.replace('x',str(num))
    return eval(to_evaluate) == val

num, val = map(int,input().split())    
polynomial = input()
print(polynomial_evaluation(*map(int,input().split())))