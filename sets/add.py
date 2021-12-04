# Enter your code here. Read input from STDIN. Print output to STDOUT
def count_unique_countries():
    n = int(input())
    countries = set()
    for i in range(n):
        country = input()
        if country not in countries:
            countries.add(country)
    print(len(countries))


def parse_input():
    input()
    a = set(map(int,input().split()))
    input()
    b = set(map(int,input().split()))
    return a, b

if __name__ == '__main__':
    count_unique_countries()
