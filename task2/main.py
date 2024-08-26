count = 0
start = 30
end = 60

print("Цілі числа, кратні трьом, в діапазоні від", start, "до", end, ":")
for val in range(start, end) : 
    if val % 3 == 0 : 
        print(val)
        count += 1
print("Кількість кратних чисел:", count)