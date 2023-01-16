L1=[1,2,3,4,5]
L2=[6,7,8,9]
print(L1+L2)


summed_lists = [ x+y for x, y in zip(L1, L2) ]
