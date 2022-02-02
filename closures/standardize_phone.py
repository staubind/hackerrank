def wrapper(f):
    def fun(l):
        # complete the function
        # need to process the input here
        lst = ['+91 ' + item[-10:-5] + ' ' + item[-5:] for item in l]
        return f(lst)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


