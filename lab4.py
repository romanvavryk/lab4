from tabulate import tabulate
import pandas as pd

f_string = [i.strip('\n').split(',') for i in open('data.txt')]
# df = pd.DataFrame(data=f_string)
# print(df)

for i in range(0, 5):
	for j in range(1, 7):
		f_string[i][j] = float(f_string[i][j])

for i in range(0, 5):
	weight = f_string[i][1]
	for j in range(2, 7):
		f_string[i][j] = round(f_string[i][j] * weight, 2) 

lst = []
for i in range(0, 5):
	new_list = []
	for j in range(1, 7):
		temp_value = f_string[i][j]
		new_list.append(temp_value)
	lst.append(new_list)


sumindex = [round(sum(elts), 2) for elts in zip(*lst)]
sumindex.insert(0, 'SUM')

f_string.append(sumindex)
# print(f_string)

for i in range(0, 6):
	max_value = 0.15
	for j in range(1, 7):
		if f_string[i][j] > max_value:
			max_value = f_string[i][j]
		else:
			continue
	f_string[i].append(max_value)

headers = ['Parameter', 'Weight', 'Adidas', 'Puma', 'Saucony', 'Dr.Martens', 'Converse', 'Max']

f_string.insert(0, headers)

df = pd.DataFrame(data=f_string)

print(df)