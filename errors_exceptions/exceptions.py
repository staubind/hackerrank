# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

for num in range(n):
    try:
        a, b = map(int,input().split())
        print(a//b)
    except ZeroDivisionError as error:
        print('Error Code: ' + str(error))
    except ValueError as error:
        print('Error Code: ' + str(error))
