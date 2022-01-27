# C-5. 3歳以下の入場料金の無料化
# 3歳以下の入場料金は無料にしてください


class Customer:
    def __init__(self, first_name, family_name, age):
        self.firstname = first_name
        self.family_name = family_name
        self.age = age

    def entry_fee(self):
        # 3歳以下の入場料金は無料にしてください
        if self.age <= 3:
            return 0
        elif self.age < 20:
            return 1000
        elif self.age < 65:
            return 1500
        # 75歳以上の入場料金は500円にしてください
        elif 65 <= self.age < 75:
            return 1200
        # 75歳以上の入場料金は500円にしてください
        else:
            return 500

    def info_csv(self):
        print(str(self.firstname) + " " + str(self.family_name) + "," + str(self.age) + "," + str(self.entry_fee()))
