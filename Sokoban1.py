map = {
    "size_x": 6,
    "size_y": 6
}

wall = [
    {"x": 0, "y": 1},
    {"x": 0, "y": 2},
    {"x": 0, "y": 3},
    {"x": 0, "y": 4},
    {"x": 0, "y": 5},
    {"x": 1, "y": 0},
    {"x": 2, "y": 0},
    {"x": 3, "y": 0},
    {"x": 4, "y": 0},
    {"x": 5, "y": 0},
    {"x": 0, "y": 0},
    {"x": 5, "y": 5},
    {"x": 5, "y": 4},
    {"x": 5, "y": 3},
    {"x": 5, "y": 2},
    {"x": 5, "y": 1},
    {"x": 5, "y": 5},
    {"x": 4, "y": 5},
    {"x": 3, "y": 5},
    {"x": 2, "y": 5},
    {"x": 1, "y": 5},

]

player = {
    "x": 3,
    "y": 4
}

boxes = [
    {"x": 2, "y": 1},
    {"x": 2, "y": 2},
    {"x": 3, "y": 3}
]

destination = [
    {"x": 3, "y": 1},
    {"x": 3, "y": 2},
    {"x": 4, "y": 3}
]
while True:
    for y in range(map["size_x"]):
        for x in range(map["size_y"]):

            wall_is_here = False
            for w in wall:
                if w["x"] == x and w["y"] == y:
                    wall_is_here = True

            box_is_here = False
            for box in boxes:
                if box["x"] == x and box["y"] == y:
                    box_is_here = True

            player_is_here = False
            if x == player["x"] and y == player["y"]:
                player_is_here = True

            dest_is_here = False
            for dest in destination:
                if dest["x"] == x and dest["y"] == y:
                    dest_is_here = True

            if x == player["x"] and y == player ["y"]:
                print(" P ", end="")
            elif wall_is_here:
                print(" W ", end="")
            elif dest_is_here:
                print(" D ", end="")
            elif box_is_here:
                print(" B ", end="")
            else:
                print(" - ", end="")
        print()
    win = True
    for box in boxes:
        if box not in destination:
            win = False
    if win:
        print("You win")
        break
    dx = 0
    dy = 0
    move = True
    movement = input("Your move: ").lower()
    if movement == "w":
        check = 0
        for box in boxes:
            for w in wall:
                if(player["y"] - 2 == box["y"] - 1 == w["y"]) and player["x"] == box["x"] == w["x"]:
                        check = 1
                for box2 in boxes:
                    if (player["y"] - 2 == box["y"] - 1 == box2["y"]) and player["x"] == box["x"] == box2["x"]:
                        check = 1
        if check == 0:
            dy = -1
            print("Left")
        elif check == 1:
            dy = 0
            print("You can't move")

    elif movement == "s":
        check = 0
        for box in boxes:
            for w in wall:
                if(player["y"] + 2 == box["y"] + 1 == w["y"]) and player["x"] == box["x"] == w["x"]:
                        check = 1
                for box2 in boxes:
                    if (player["y"] + 2 == box["y"] + 1 == box2["y"]) and player["x"] == box["x"] == box2["x"]:
                        check = 1
        if check == 0:
            dy = 1
            print("Left")
        elif check == 1:
            dy = 0
            print("You can't move")
    elif movement == "a":
        check = 0
        for box in boxes:
            for w in wall:
                if(player["x"] - 2 == box["x"] - 1 == w["x"]) and player["y"] == box["y"] == w["y"]:
                        check = 1
                for box2 in boxes:
                    if (player["x"] - 2 == box["x"] - 1 == box2["x"]) and player["y"] == box["y"] == box2["y"]:
                        check = 1
        if check == 0:
            dx = -1
            print("Left")
        elif check == 1:
            dx = 0
            print("You cant move")

    elif movement == "d":
        check = 0
        for box in boxes:
            for w in wall:
                if(player["x"] + 2 == box["x"] + 1 == w["x"]) and player["y"] == box["y"] == w["y"]:
                        check = 1
                for box2 in boxes:
                    if (player["x"] + 2 == box["x"] + 1 == box2["x"]) and player["y"] == box["y"] == box2["y"]:
                        check = 1
        if check == 0:
            dx = 1
            print("Left")
        elif check == 1:
            dx = 0
            print("You can't move")
    else:

        print("Wrong key! Try again")
        break

    if (0 < player["x"] + dx < map["size_x"] - 1 and 0 < player["y"] + dy < map["size_y"] - 1) and (0 < box["x"] + dx < map["size_x"] and 0 < box["y"] + dy < map["size_y"]):

            player["x"] += dx
            player["y"] += dy

    for box in boxes:

        if player["x"] == box["x"] and player["y"] == box["y"]:
            box["x"] += dx
            box["y"] += dy