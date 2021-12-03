
# example:
# 'AAABCADDE' => 
# A
# BCA
# DE
# allowed to assume len(string)%k == 0


def merge_the_tools(string, k):
    for i in range(int(len(string)/k)):
        start = i * k
        end = start + k
        substring = string[start:end]
        uniques = set()
        u_sub = ''
        # find the unique version of the substring
        for j in range(k):
            current = substring[j]
            if current not in uniques:
                u_sub += current
                uniques.add(current)
        print(u_sub)

merge_the_tools('AABCAAADA', 3)