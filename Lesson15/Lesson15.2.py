class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # def correct_fraction(self):
    #     if self.a >= self.b:
    #         raise ValueError("Число >= 1")
    #     elif self.b == 0:
    #         raise ValueError("знам == 0")
    #     else:
    #         print("Работаем")

    def __mul__(self, other):
        return Fraction(self.a * other.a , self.b * other.b)

    def __add__(self, other):
        if self.b == other.b:
            return Fraction(self.a + other.a, self.b )
        else:
            return Fraction(self.a * other.b + self.b * other.a, self.b * other.b)


    def __sub__(self, other):
        if self.b == other.b:
            return Fraction(self.a - other.a, self.b)
        else:
            return Fraction(self.a * other.b - self.b * other.a, self.b * other.b)

    def __eq__(self, other):
        if self.b == other.b:
            return self.a == other.a
        else:
            return self.a * other.b == self.b * other.a

    def __gt__(self, other):
        if self.b == other.b:
            return self.a > other.a
        else:
            return self.a * other.b > self.b * other.a

    def __lt__(self, other):
        if self.b == other.b:
            return self.a < other.a
        else:
            return self.a * other.b < self.b * other.a

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
#print(Fraction(f_a, f_b))

# print(f_a.correct_fraction())
# print(f_b.correct_fraction())

f_c = f_b + f_a
#print(f_c)
assert str(f_c) == 'Fraction: 21, 18'

f_d = f_b * f_a
#print(f_d)
assert str(f_d) == 'Fraction: 6, 18'

f_e = f_a - f_b
#print(f_e)
assert str(f_e) == 'Fraction: 3, 18'

#print(f_d < f_c)
#print(f_d > f_e)
#print(f_a != f_b )
assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True

f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
#print(f_1 == f_2)
assert f_1 == f_2  # True
print('OK')