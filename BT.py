from turtle import *

# for _ in range(4):
#     forward(50)
#     left(90)

# for _ in range(3):
#     for a in range(4):
#         forward(50)
#         left(90)
#     right(30)

# for _ in range(20):
#     for b in range(4):
#         forward(50)
#         left(90)
#     right(30)

speed(-1)
for i in range(100):
    for c in range(4):
        forward(2*i)
        left(90)
    right(30)


mainloop()