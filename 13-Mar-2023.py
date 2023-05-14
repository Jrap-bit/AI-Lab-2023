import random


class Wumpus:
    def __init__(self):
        self.env = [[" " for x in range(5)] for y in range(5)]
        self.gold_pos = [2, 4]
        self.wumpus_pos = [3, 1]
        self.gold_found = False
        self.dead = False
        self.path = []
        self.current_pos = [0, 0]
        self.info = [[" " for x in range(5)] for y in range(5)]
        self.actions = ["move_up", "move_down", "move_left", "move_right"]

    def create_env_mat(self):
        self.env[0][4] = "B"
        self.env[1][3] = "B"
        self.env[1][4] = "P"
        self.env[2][4] = "B"
        self.env[2][4] = "B"
        self.env[3][3] = "B"
        self.env[3][4] = "P"
        self.env[4][4] = "B"
        self.env[self.wumpus_pos[0] - 1][self.wumpus_pos[1]] = "S"
        self.env[self.wumpus_pos[0] + 1][self.wumpus_pos[1]] = "S"
        self.env[self.wumpus_pos[0]][self.wumpus_pos[1] + 1] = "S"
        self.env[self.wumpus_pos[0]][self.wumpus_pos[1] - 1] = "S"
        self.env[self.wumpus_pos[0]][self.wumpus_pos[1]] = "W"

    def display(self):
        for x in range(len(self.env)):
            for y in range(len(self.env[0])):
                if x == self.gold_pos[0] and y == self.gold_pos[1]:
                    print(self.env[x][y] + "/G", end=" ")
                else:
                    if self.env[x][y] == " ":
                        print("_", end=" ")
                    else:
                        print(self.env[x][y], end=" ")
            print()

    def display_info(self):
        for x in range(len(self.info)):
            for y in range(len(self.info[0])):
                if self.env[x][y] == " ":
                    print("_", end=" ")
                else:
                    print(self.info[x][y], end=" ")
            print()

    def move_down(self):
        if self.current_pos[0] >= 4:
            return
        self.current_pos[0] += 1
        self.path.append("down")

    def move_up(self):
        if self.current_pos[0] <= 0:
            return
        new_loc = [self.current_pos[0]-1, self.current_pos[1]]
        if (self.info[new_loc[0]][new_loc[1]] == "Safe"):
            self.current_pos[0] -= 1
            self.path.append("up")
        elif(self.info[new_loc[0]][new_loc[1]] == "Safe"):
            # To be edited
            pass

    def move_left(self):
        if self.current_pos[1] <= 0:
            return
        self.current_pos[1] += 1
        self.path.append("left")

    def move_right(self):
        if self.current_pos[1] >= 4:
            return
        self.current_pos[1] -= 1
        self.path.append("right")

    def back_track(self):
        move = self.path[-1]
        if move == "up":
            self.current_pos[0] += 1
            self.path.append("down")
        elif move == "down":
            self.current_pos[0] -= 1
            self.path.append("up")
        elif move == "left":
            self.current_pos[1] += 1
            self.path.append("right")
        elif move == "right":
            self.current_pos[1] -= 1
            self.path.append("left")

    def check(self):
        if self.env[self.current_pos[0]][self.current_pos[1]] == "B":
            self.info[self.current_pos[0]][self.current_pos[1]] = "B"
            return "back"
        elif self.env[self.current_pos[0]][self.current_pos[1]] == "S":
            self.info[self.current_pos[0]][self.current_pos[1]] = "S"
            return "back"
        elif self.env[self.current_pos[0]][self.current_pos[1]] == "W":
            self.info[self.current_pos[0]][self.current_pos[1]] = "W"
            return "dead"
        elif self.env[self.current_pos[0]][self.current_pos[1]] == "P":
            self.info[self.current_pos[0]][self.current_pos[1]] = "P"
            return "dead"
        else:
            self.info[self.current_pos[0]][self.current_pos[1]] = "Safe"
            return "safe"

    def percept(self):
        while not self.gold_found:
            if self.current_pos[1] == -6:
                print(self.path)
            try:
                if self.env[self.current_pos[0]][self.current_pos[1]] == "G":
                    self.gold_found = True
                    self.info[self.current_pos[0]][self.current_pos[1]] = "G"
                    print("Gold Found")
                    print("Path: ", self.path)
                    break
            except IndexError:
                print(self.current_pos)
                break
            else:
                try:
                    action = random.choice(self.actions)
                    if action == "move_up":
                        self.move_up()
                    elif action == "move_down":
                        self.move_down()
                    elif action == "move_left":
                        self.move_left()
                    elif action == "move_right":
                        self.move_right()
                    act = self.check()
                    if act == "back":
                        self.back_track()
                    elif act == "dead":
                        print("You are dead")
                    elif act == "safe":
                        continue
                except IndexError:
                    continue


if __name__ == "__main__":
    obj1 = Wumpus()
    obj1.create_env_mat()
    obj1.display()
    obj1.percept()
    obj1.display_info()