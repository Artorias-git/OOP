Size = 6
Winline = 4



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