lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
lst_one = []

# variant 1
for i in range(len(lst) - 1):
    if lst[i + 1] > lst[i]:
        lst_one.append(lst[i + 1])

# variant 2
lst_two = [lst[i + 1] for i in range(len(lst) - 1) if lst[i + 1] > lst[i]]

# variant 3
lst = [lst[i + 1] for i in range(len(lst) - 1) if lst[i + 1] > lst[i]]

print(f'decision 1: {lst}')
print(f'decision 2: {lst_one}')
print(f'decision 3: {lst_two}')
