class Customer:
    def __init__(self, first_name, family_name, age):
        self.firstname = first_name
        self.family_name = family_name
        self.age = age

    def entry_fee(self):
        if self.age < 20:
            return 1000
        elif self.age < 65:
            return 1500
        else:
            return 1200

    def info_csv(self):
        print(str(self.firstname) + " " + str(self.family_name) + "," + str(self.age) + "," + str(self.entry_fee()))


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age=57)
tom.info_csv()  # "Tom Ford,57,1500" という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す
