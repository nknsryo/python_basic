sequence = input("データを入力してください(スペース区切り) >").split()


# 合計値
def total():
    sequence_total = 0
    for sequence_count in range(0, len(sequence)):
        sequence_total += int(sequence[sequence_count])
    return sequence_total


print(f"合計値: {total()}")

# 最大値
# print(f"最大値: {max(sequence)}")
sequence_max = int(sequence[0])
for sequence_count in range(1, len(sequence)):
    if int(sequence[sequence_count]) >= sequence_max:
        sequence_max = int(sequence[sequence_count])
    else:
        pass
print(f"最大値: {sequence_max}")

# 最小値
# print(f"最小値: {min(sequence)}")
sequence_min = int(sequence[0])
for sequence_count in range(1, len(sequence)):
    if int(sequence[sequence_count]) <= sequence_min:
        sequence_min = int(sequence[sequence_count])
    else:
        pass
print(f"最小値: {sequence_min}")

# 平均値
print(f"平均値: {total() / len(sequence)}")

