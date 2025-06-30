ls = [1,2,3,4,5,6,7,8,9,10]
f_fi = ls[0:5]           # f_fi = [1, 2, 3, 4, 5]
rev = f_fi[::-1]
print("Originlas list:" , ls)
print("First five elements: " ,f_fi)
print("Reversed list is: " , rev)



# rev = f_fi[::-1]  # dont change th eorder
# print("rev" , rev)
# rev = f_fi[::-1]         # rev = [5, 4, 3, 2, 1] - reversed copy
# print("rev", rev)        # print the reversed list
# print("original", f_fi)  # original list still intact
#f_fi.reverse()