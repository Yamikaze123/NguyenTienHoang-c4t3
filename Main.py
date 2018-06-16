import Bai_1 as one
import Bai_2 as two
import Bai_3 as three
import Bai_4 as four

try:
    n = int(input("Input your number:"))
except:
    n = None

if n == None:
    print("Ban nhap sai roi")
else:
    Bai_1_result = one.list(n)
    print("Ket qua bai 1: ", Bai_1_result)

Bai_2_result = two.exponential()
print("Ket qua bai 2: ", Bai_2_result)

x = [0, -1, 2, -3, 4, -5, 6]

Bai_3_result = three.trigonometry(x)
print("Ket qua bai 3: ", Bai_3_result)

Bai_4_result = four.sum_absolute(x)
print("Ket qua bai 4: ", Bai_4_result)
