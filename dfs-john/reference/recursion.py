# factorial recursion
# f(n!) = n * (n -1 )

# def fact(n):
#     if (n >= 1 ):
#         return n * fact(n - 1)
#     return 1


# given = int(input("enter int: "))
# print(fact(given))







#sum of natural numbers problem. 
def sum_n(n, counter):
    if(n > 0):
        counter = n + sum_n(n -1, counter)
    return counter


result = sum_n(5, 0)
print(result)


#better solution
def sum_c(n):
    if n == 0:
        return 0
    return n + sum_c(n - 1)

#recursive string
def reverse_string(s):
    joined = []
    string_list = list(s)
    
    
    # return s.reverse()


result = reverse_string("hello")
print(f'reversed string: {result}')