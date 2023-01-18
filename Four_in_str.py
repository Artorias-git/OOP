Size = 6
Winline = 4
field = [[0 for x in range(Size)] for x in range(Size)]

# def vertical_horizontal_check(field):
#     token = 0
#     for i in range(Size):
#         for j in range(1, Size):
#             if (field[i][j] == field[i][j-1]) and (field[i][j] != 0):
#                 token += 1
#                 if token == Winline -1:
#                     return True
#             else:
#                 token = 0
#             token = 0
#             if (field[j][i] == field[j][i - 1]) and (field[j][i] != 0):
#                 token += 1
#                 if token == Winline - 1:
#                     return True
#             else:
#                 token = 0
#     return False

# def diagonal_check(field):
#     a = 1
#     token = 0
#     for i in range(Winline - 2, Size - 2):
#         if field[i][a] == field[i - 1][a - 1] and (field[i][a] != 0):
#             token += 1
#             if token == Winline - 1:
#                 return True
#         else:
#             token = 0
#         a += 1
#     return False
class Player():
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def rename(self, new_name):
        self.__name = new_name


    @property
    def name(self):
        return self.__name


p1 = Player("Ayur", 4)
p2 = Player("Kostya", 6)

players = [p1, p2]








def Print(field, Size):
    for i in range(Size):
        print(field[i])
    print("\n")

def vertical_horizontal_check2(field, str, stolb, player):
    val = field[str][stolb]
    x = stolb
    token = 0
    i = 1
    # горизонтально
    while x - i >= 0:  # по горизонтали влево
        if field[str][x - i] == val:
            token += 1
        else:
            break
        i += 1
    i = 1
    while x + i < Size:  # по горизонтали вправо
        if field[str][x + i] == val:
            token += 1
        else:
            break
        i += 1
    if token >= Winline - 1:
        Game_over(player)
    #вертикально
    token = 0
    i = 1
    x = str
    while x - i >= 0:  # по вертикали вверх
        if field[x - i][stolb] == val:
            token += 1
        else:
            break
        i += 1
    i = 1
    while x + i < Size:  # по вертикали вниз
        if field[x + i][stolb] == val:
            token += 1
        else:
            break
        i += 1
    if token >= Winline - 1:
        Game_over(player)

def diagonal_check2(field, str, stolb, player):
    val = field[str][stolb]
    y = str
    x = stolb
    i = 1
    token = 0
    while (x - i >= 0) and (y + i < Size):    # влево вниз
        if field[y + i][x - i] == val:
            token += 1
        else:
            break
        i += 1
    i = 1
    while (x + i < Size) and (y - i >= 0):  # вправа вверх
        if field[y - i][x + i] == val:
            token += 1
        else:
            break
        i += 1
    if token >= Winline - 1:
        Game_over(player)
    i = 1
    token = 0
    while (x + i < Size) and (y + i < Size):  # вправа вниз
        if field[y + i][x + i] == val:
            token += 1
        else:
            break
        i += 1
    i = 1
    while (x - i >= 0) and (y - i >= 0):  # влево вверх
        if field[y - i][x - i] == val:
            token += 1
        else:
            break
        i += 1
    if token >= Winline - 1 :
        Game_over(player)
# проверка заполненности
def Full_check(field):
    token = 0
    for i in range(Size):
        for j in range(Size):
            if field[i][j] == 0:
                token += 1
    if token == 0:
        Game_over(3)

# ввод столбца с проверкой
def Input_checked(field, player):
    while True:
        arr = []
        target = int(input("номер столбца: "))
        for i in range(Size):
            if field[i][target - 1] == 0:
                arr.append(i)
        if len(arr) < 1:
            print("этот столбец полон")
            continue
        else:
            field[arr[len(arr)-1]][target - 1] = player
            return arr[len(arr)-1], target

    # if target == "":
    #     print("Try again")
    #     Input_checked(field, player)
    # if (target < 1) or (target > 6):
    #     print("Try again")
    #     Input_checked(field, player)
    # for i in range(Size - 1, -1, -1):
    #         if field[i][target - 1] == 0:
    #             field[i][target - 1] = player
    #             return i, target # возвращаем координаты новой клетки
    # print("Try again")
    # Input_checked(field, player)

def Game_over(player):
    Print(field, Size)
    if player == 3:
        print("Ничья")
        exit()
    else:
        print("Игрок ", player," Победил!!!")
        exit()

def update_check(player, field):
    print("Ход игрока - ", player)
    a = Input_checked(field, player)

    print("\n")
    vertical_horizontal_check2(field, a[0], a[1] - 1, player)
    diagonal_check2(field, a[0], a[1] - 1, player)
    Full_check(field)
    print("\n")

    if player == 1:
        player = 2
    else:
        player = 1
    Print(field, Size)
    update_check(player, field)

Print(field, Size)
player = 1
update_check(player, field)
