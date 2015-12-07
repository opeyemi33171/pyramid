number_of_rows = int(input("Please enter the number of rows"))
for i in range(1, number_of_rows + 1):
    if not i % 2 == 0:
        print("#"*i)