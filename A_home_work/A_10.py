# import random
#
# dice = [1, 2, 3, 4, 5, 6]
#
# print(random.choice(dice))  # 1から6の整数をランダムに出力する
import random


def dice_random():
    result = random.randint(1, 6)
    return result


print(dice_random())
