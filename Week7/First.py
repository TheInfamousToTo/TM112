tables = [[9, 27, 26, 19, 12, 7],[5,8,44,99,66,145,5]]
total = 0
for row in range (len(tables)):
    numbers=tables[row]
    total=0
    for rating in range(len(tables)):
        product = rating * numbers[rating]
        total = total + product
    average = total / sum(tables[row])
    print('average rating =', average)

