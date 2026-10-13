# create a tuple with different data types
tuplex = ("turple", False , 3.2 ,1)
print(tuplex)

#create a tuple
tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)
# turples are immutable, so you cannot add new elements
turple1 = (50,10,60,70,50)
print(turple1.count(50))

#create a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
#used tuple [start:stop] the start index is inclusive and the stop index
_slice = tuplex[3:5]
#is exclusive
print(_slice)
#if the start index is not defined, is taken from the beginning of the tuple
_slice = tuplex[:6]
print(_slice)
