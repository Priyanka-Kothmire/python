# l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
# output = []
# # sum=0
# i=0
# while i<len(l):
#     j=0
#     while j<len(l):
#         # output.append(l)
#         # sum=sum+l[i][j]
#         output.append(l[i][j])

#         j=j+1
#     i=i+1
# print(output)


# l = [1, 2, [3, 4, [5, 6]], 15, 8, [9, [10]]]
  
# # output list
# output = []
  
# # function used for removing nested 
# # lists in python. 
# def reemovNestings(l):
#     for i in l:
#         if type(i) == list:
#             reemovNestings(i)
#         else:
#             output.append(i)
  
# # Driver code
# print ('The original list: ', l)
# reemovNestings(l)
# print ('The list after removing nesting: ', output)



l = [1, 2, [3, 4, [5, 6]], 15, 8, [9, [10]]]
i=0  
output = []
sum=0
while i<len(l):
    j=0
    while j<len(l[i]):
        sum=sum+l[i][j]
    j=j+1
i=i+1
print(sum)





