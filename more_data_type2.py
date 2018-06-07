x1 = int(input("Hoanh do tam 1"))
y1 = int(input("Tung do tam 1"))
r1 = float(input("Ban kinh 1"))
x2 = int(input("Hoanh do tam 2"))
y2 = int(input("Tung do tam 2"))
r2 = float(input("Ban kinh 2"))

center_distance = ((x1-x2)**2+(y1-y2)**2)**1/2

if center_distance < (r1+r2):
    print("2 hinh tron overlap")
else:
    print("2 hinh tron khong overlap")