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
for sequence_count in range(0, len(sequence)):
    sequence_compare = sequence[sequence_count]
    if sequence_compare

# 最小値
# print(f"最小値: {min(sequence)}")

# 平均値
print(f"平均値: {total() / len(sequence)}")
