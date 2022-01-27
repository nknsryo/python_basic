# 次のコードが正しく動作するような Square クラスを実装してください
# diagonal は 対角線(の長さ) という意味です。

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def diagonal(self):
        return f"{self.side * 2 ** 0.5:.2f}"


square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21
