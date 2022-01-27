# Enter your code here. Read input from STDIN. Print output to STDOUT

# truncate to shortest list length
# returns list of tuples of ith element of each iterable


def get_input():
    x,n = map(int,input().split())
    subjects_scores = [list(map(float, input().split())) for i in range(n)]
    return list(zip(*subjects_scores))

def process_data(scores):
    averages = [sum(item)/len(item) for item in scores]
    for avg in averages:
        print(avg)
    return averages

student_scores = get_input()
process_data(student_scores)