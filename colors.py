#print out all colors from color-list1 not contained in color-list2.

color_list1 = set(["White", "Black", "Red"])
color_list2 = set(["Red", "Green"])
print([i for i in color_list1 if i not in color_list2])
