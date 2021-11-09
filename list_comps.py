if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    lexicographic_permutations = list(filter(lambda a: len(a) != 0,
        [[i,j,k] if i+j+k != n else [] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) ]    
        )) # I learned you can simply place an if <some_condition> clause at the end of a list comp like this
        #awesome! learning :)
    print(lexicographic_permutations)