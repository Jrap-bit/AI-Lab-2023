def check_battery():
    global current_charge, current_location, last_location_served, distance_Charge_Point
    if current_charge == distance_Charge_Point:
        last_location_served = current_location
        recharge()
    else:
        pass


def recharge():
    global current_charge, time_taken, current_location
    while current_location[0] != 0:
        current_location[0] -= 1
        visited[current_location[0]][current_location[1]] = True
        current_charge -= 1
        time_taken += 1

    while current_location[1] != 0:
        current_location[1] -= 1
        visited[current_location[0]][current_location[1]] = True
        current_charge -= 1
        time_taken += 1

    current_location = last_location_served


def pot_found():
    global distance_Charge_Point, time_taken, current_location
    update_distance_from_cp(current_location[0], current_location[1])
    if current_location[0] == int(gold_x) and current_location[1] == int(gold_y):
        time_taken += distance_Charge_Point
        return True
    else:
        return False


def update_distance_from_cp(x, y):
    global distance_Charge_Point
    distance_Charge_Point = x+y


def start():
    global time_taken, current_charge
    while not pot_found():
        check_battery()
        if current_location[1] % 2 == 0:
            if current_location[0] == room_dimensions - 1:
                current_location[1] += 1
                time_taken += 1
                current_charge -= 1
            else:
                current_location[0] += 1
                time_taken += 1
                current_charge -= 1
                visited[current_location[0]][current_location[1]] = True
        else:
            if current_location[0] == 0:
                current_location[1] += 1
                time_taken += 1
                current_charge -= 1
            else:
                current_location[0] -= 1
                time_taken += 1
                current_charge -= 1
                visited[current_location[0]][current_location[1]] = True


if __name__ == "__main__":
    room_dimensions = 5  # N
    max_charge = 22  # X
    room = [["_" for x in range(room_dimensions)] for y in range(room_dimensions)]  # Room Matrix Representation
    visited = [[False for x in range(room_dimensions)] for y in range(room_dimensions)]  # If the Room is Visited or Not
    current_charge = max_charge
    current_location = [0, 0]
    last_location_served = [0, 0]
    distance_Charge_Point = current_location[0] + current_location[1]
    gold_pot = input("Enter a location for Gold Pot: ")
    gold_x, gold_y = gold_pot.split(" ")
    room[int(gold_x)][int(gold_y)] = "G"
    room[0][0] = "S"
    visited[0][0] = True
    time_taken = 0
    start()
    for i in room:
        print(i)
    print(time_taken)
