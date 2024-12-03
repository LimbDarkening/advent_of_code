import pandas as pd

ls1 = []
ls2 = []
with open ("input.txt") as file:
	for line in file:
		one, two = line.split()
		ls1.append(int(one))
		ls2.append(int(two))
#print(ls1)
#print(ls2)

array_1 = pd.Series(sorted(ls1))
array_2 = pd.Series(sorted(ls2))
#print((array_1-array_2).abs().sum())

# problem 2

counts = array_2.value_counts().to_dict()

res = [i * counts.get(i,0) for i in array_1.to_list()]
print(sum(res))

