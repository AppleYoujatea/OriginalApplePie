def solution(numbers, hand):

    keypad = {
        1: [0, 0],
        2: [1, 0],
        3: [2, 0],
        4: [0, 1],
        5: [1, 1],
        6: [2, 1],
        7: [0, 2],
        8: [1, 2],
        9: [2, 2],
        "*": [0, 3],
        0: [1, 3],
        "#": [2, 3],
    }

    l_now = "*"
    r_now = "#"

    route = []

    for i in range(len(numbers)):
        if str(numbers[i]) in "147":
            l_now = numbers[i]
            route.append("L")
        elif str(numbers[i]) in "369":
            r_now = numbers[i]
            route.append("R")
        else:  # numbers[i] in 2580
            target_x, target_y = keypad[numbers[i]]
            l_x, l_y = keypad[l_now]
            r_x, r_y = keypad[r_now]

            l_calc = abs(target_x - l_x) + abs(target_y - l_y)
            r_calc = abs(target_x - r_x) + abs(target_y - r_y)


            if l_calc < r_calc:
                l_now = numbers[i]
                route.append("L")
            elif r_calc < l_calc:
                r_now = numbers[i]
                route.append("R")
            else:  # l_calc == r_calc
                if hand == "left":
                    l_now = numbers[i]
                    route.append("L")
                elif hand == "right":
                    r_now = numbers[i]
                    route.append("R")

    answer = "".join(route)
    return answer