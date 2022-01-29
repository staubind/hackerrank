def fibonacci(n):
    # return a list of fibonacci numbers
    fibs = [0,1]
    if n == 0:
        return []
    if n == 1:
        return fibs[:1]
    for i in range(2,n):
        fibs.append(fibs[i-1]+fibs[i-2])
    return fibs
    
cube = lambda x: x**3
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))