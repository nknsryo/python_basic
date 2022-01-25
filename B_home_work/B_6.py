# 課題B-6: N面サイコロの反復試行
# N面サイコロをM回振ったときの結果を表示してください
# N, M は正の整数とします
# N, M はユーザーからの入力を利用すること


import random

# サイコロの面の数をユーザーに要求
total_daice_side = int(input(f"サイコロの面の数は？: "))
# 面に記載されている数をランダムに表示する
daice_number = random.randint(1, total_daice_side)

# サイコロを振る回数をユーザーに要求
daice_action_times = int(input(f"何回振りますか?: "))

# for daice in range(0, daice_action_times):
#     for daice_number in range(0, total_daice_side):
#         daice = list(str(random.randint(1, total_daice_side)))
#     print(f"{daice}", end=' ')

daice = []
for result in range(0, daice_action_times):
    daice.append(random.randint(1, total_daice_side))
print(daice)
