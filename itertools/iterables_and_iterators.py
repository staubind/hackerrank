# based on the actual description of the problem the following commented out code
# yields the correct results.
# however, based on the examples and test cases, they mean to ask a different
# question, which i have answered below all of this.
# len_n = int(input())
# n = input().split()
# k = int(input())

# def prob_of_an_a(char_list, choose_k):
#     count_a = 0
#     total = len(char_list)
#     for letter in char_list:
#         if letter == 'a':
#             count_a += 1
#     q = 1 - count_a / total
#     # 1 - p(o) = 1 - (total choose 0 8 p**0 * (1-p)**total)
#     return 1 - (q)**total
    
# print(prob_of_an_a(n,k))