rows = int(input("行数を入力してください: "))
cullums = int(input("列数を入力してください: "))

for count_rows in range(1, rows + 1):
    for count_cullums in range(1, cullums + 1):
        print(count_rows * count_cullums, end=' ')
    print()
