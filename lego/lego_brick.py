# encoding=utf-8
import random


class Floor:
    def __init__(self, n):
        self.floor_len = 2 ** n
        self.floor = [[0 for _ in range(self.floor_len)] for _ in range(self.floor_len)]

    def show_floor(self):
        for i in range(self.floor_len):
            for j in range(self.floor_len):
                print(self.floor[i][j], end='  ')
            print()

        for i in range(self.floor_len):
            print('-', end='  ')

        print()

    def get_brick_sign(self, spot):
        return self.floor[spot.x][spot.y]

    def set_brick_sign(self, spot, sign):
        self.floor[spot.x][spot.y] = sign

    def set_4_brick_sign(self, spot, sign):
        self.floor[spot.x][spot.y] = sign
        self.floor[spot.x+1][spot.y] = sign
        self.floor[spot.x][spot.y+1] = sign
        self.floor[spot.x+1][spot.y+1] = sign



def brick_factory():
    def context():
        brick_start_sign = ord('0')
        def wrapper():
            nonlocal brick_start_sign
            brick_start_sign += 1
            # if brick_start_sign == ord('9')+1:
            #     brick_start_sign = ord('a')
            return chr(brick_start_sign)
        return wrapper
    return context()


class Spot:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def brick_paving(floor, start_spot, spot, length, brick_sign):
    if length == 2:
        spot_brick_sign = floor.get_brick_sign(spot)
        floor.set_4_brick_sign(start_spot, brick_sign())
        floor.set_brick_sign(spot, spot_brick_sign)
        floor.show_floor()
    else:
        length_2 = int(length/2)
        middle_x = start_spot.x + length_2
        middle_y = start_spot.y + length_2
        start_spot_11 = start_spot
        start_spot_12 = Spot(start_spot.x, middle_y)
        start_spot_21 = Spot(middle_x, start_spot.y)
        start_spot_22 = Spot(middle_x, middle_y)
        tmp = [[0, 0], [0, 0]]
        if spot.x < middle_x:
            tmp[1][0] = 1
            tmp[1][1] = 1
        else:
            tmp[0][0] = 1
            tmp[0][1] = 1

        if spot.y < middle_y:
            tmp[0][1] = 1
            tmp[1][1] = 1
        else:
            tmp[0][0] = 1
            tmp[1][0] = 1
        sign = brick_sign()
        if tmp[0][0]:
            spot_11 = Spot(middle_x-1, middle_y-1)
            floor.set_brick_sign(spot_11, sign)
        else:
            spot_11 = spot

        if tmp[0][1]:
            spot_12 = Spot(middle_x - 1, middle_y)
            floor.set_brick_sign(spot_12, sign)
        else:
            spot_12 = spot

        if tmp[1][0]:
            spot_21 = Spot(middle_x, middle_y-1)
            floor.set_brick_sign(spot_21, sign)
        else:
            spot_21 = spot

        if tmp[1][1]:
            spot_22 = start_spot_22
            floor.set_brick_sign(spot_22, sign)
        else:
            spot_22 = spot
        floor.show_floor()
        brick_paving(floor, start_spot_11, spot_11, length_2, brick_sign)
        brick_paving(floor, start_spot_12, spot_12, length_2, brick_sign)
        brick_paving(floor, start_spot_21, spot_21, length_2, brick_sign)
        brick_paving(floor, start_spot_22, spot_22, length_2, brick_sign)


if __name__ == '__main__':
    # 地面生成
    floor = Floor(3)
    floor.show_floor()

    # 自动砖的样式生成
    brick_sign = brick_factory()

    # 随机一块砖的选取
    x = random.randint(0, floor.floor_len - 1)
    y = random.randint(0, floor.floor_len - 1)
    floor.floor[x][y] = brick_sign()
    floor.show_floor()
    # 铺砖
    start_spot = Spot(0, 0)
    spot = Spot(x, y)
    brick_paving(floor, start_spot, spot, floor.floor_len,brick_sign)
    floor.show_floor()

