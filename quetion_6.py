l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
# l = ["o", "w", ["n", "s", ["e", "l"]], "d", "c", ["b", ["a"]]]
new_list = []
def nested_list(l):
    for i in l:
        if type(i) == list:
            nested_list(i)
        else:
            new_list.append(i)
nested_list(l)
print (new_list)






