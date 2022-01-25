# 課題B-6: N面サイコロの反復試行
# N面サイコロをM回振ったときの結果を表示してください
# N, M は正の整数とします
# N, M はユーザーからの入力を利用すること


import random

# サイコロの面の数をユーザーに要求
total_daice_side = int(input(f"サイコロの面の数は？: "))

# サイコロを振る回数をユーザーに要求
daice_action_times = int(input(f"何回振りますか?: "))


daice = []
for result in range(0, daice_action_times):
    daice.append(random.randint(1, total_daice_side))
print(daice)
