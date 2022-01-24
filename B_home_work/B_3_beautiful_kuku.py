rows = int(input("行数を入力してください: "))
cullums = int(input("列数を入力してください: "))

for count_rows in range(1, rows + 1):
    for count_cullums in range(1, cullums + 1):
        counter_response = count_rows * count_cullums
        if 1 <= counter_response <= 9:
            counter_response = int(str(counter_response).rjust(0, 1))
        else:
            counter_response
            print(f"{count_cullums} ×　{count_rows} = {counter_response} ｜", end=' ')
    print()
