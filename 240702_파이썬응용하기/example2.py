with open('data/chicken.txt', 'r', encoding='UTF8') as f:
    total_revenue = 0
    total_days=  0

    for line in f:
        data = line.strip().split(": ")
        revenue = int(data[1])

        total_revenue += revenue
        total_days += 1

    print(total_revenue / total_days)


        


#split
my_string = "1.2.3.4.5.6"
print(my_string.split("."))



with open('data/new_file.txt', 'a') as f:
    f.write("Hello world!/n")