
class Ground:
    def __init__(self, size, count):
        self.__size = size
        self.__count_to_win = count
        self.__arr = [[0 for i in range(size)] for j in range(size)]

    def get_empty_row(self, colomn):
        for i in range(self.__size - 1, -1, -1):                  #здесь может быть прикол с range
            if self.__arr[i][colomn] == 0:
                return i
        print("Этот столбец полон")
        return "full"

    def update_arr(self, target_colomn, player):
        colomn = target_colomn
        number = player.number

        row = self.get_empty_row(colomn)
        if row == "full":
            print("выбирете другой столбец \n")
            return True
        self.__arr[row][colomn] = number
        self.print_ground()
        self.check_full_ground()
        self.check_wins_ground(target_colomn, row, player)
        return False

    def check_full_ground(self):
        size = self.__size
        for i in range(size):
            for j in range(size):
                if self.__arr[i][j] == 0:
                    return
        game.game_over("full ground")

    def print_ground(self):
        for i in range(self.__size):
            print(self.__arr[i])
        pass

    def check_wins_ground(self, target_colomn, row, player):
        arr = self.__arr
        value = arr[row][target_colomn]
        def gorizontal_check(arr, target_colomn, row):
            count = 1
            i = 1
            while target_colomn - i >= 0:
                if arr[row][target_colomn - i] == value:
                    count += 1
                    i += 1
                else:
                    i = 1
                    break

            while target_colomn + i < len(arr):
                if arr[row][target_colomn + i] == value:
                    count += 1
                    i += 1
                else:
                    break
            return count
        if gorizontal_check(arr, target_colomn, row) == game.count_to_win:
            game.game_over(player)

        def vertically_check(arr, target_colomn, row):
            count = 1
            i = 1
            while row - i >= 0:
                if arr[row - i][target_colomn] == value:
                    count += 1
                    i += 1
                else:
                    i = 1
                    break
            count = 1
            i = 1
            while row + i < len(arr):
                if arr[row + i][target_colomn] == value:
                    count += 1
                    i += 1
                else:
                    break
            return count
        if vertically_check(arr, target_colomn, row) == game.count_to_win:
            game.game_over(player)

        def diagonal_check1(arr, target_colomn, row):
            count = 1
            i = 1
            while (row - i >= 0) and (target_colomn - i >= 0):
                if arr[row - i][target_colomn - i] == value:
                    count += 1
                    i += 1
                else:
                    i = 1
                    break
            while (row + i < len(arr)) and (target_colomn + i < len(arr)):
                if arr[row + i][target_colomn + i] == value:
                    count += 1
                    i += 1
                else:
                    break
            return count
        if diagonal_check1(arr, target_colomn, row) == game.count_to_win:
            game.game_over(player)

        def diagonal_check2(arr, target_colomn, row):
            count = 1
            i = 1
            while (row - i >= 0) and (target_colomn + i < len(arr)):
                if arr[row - i][target_colomn + i] == value:
                    count += 1
                    i += 1
                else:
                    i = 1
                    break
            while (row + i < len(arr)) and (target_colomn - i >= 0 ):
                if arr[row + i][target_colomn - i] == value:
                    count += 1
                    i += 1
                else:
                    break
            return count
        if diagonal_check2(arr, target_colomn, row) == game.count_to_win:
            game.game_over(player)

class Player:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def number(self):
        return self.__number

class Game:
    def __init__(self, size, count):
        self.__size = size
        self.__count_to_win = count
        self.__started = False
        self.__plaers = []
        self.__ground = None
        self.__currant_player = 0
        self.__turns_count = 1
        pass

    def start_game(self):   #начинаем игру
        self.__started = True
        self.__ground = Ground(self.__size, self.__count_to_win)  #создаём поле
        N = self.number_input("Введите количество игроков: ")
        for i in range(N):
           name = self.name_input(f"игрок номер {i+1} введите имя: ")
           numbers = self.number_input("придумайте себе число от 1 до 9: ")
           self.__plaers.append(Player(name, numbers))   #регестрируем игроков

        self.__currant_player = 0
        self.turn(0)

    def turn(self, cur_player):

        player = self.__plaers[cur_player]
        print(f"Ход игрока {player.name} ")
        target_colomn = self.turn_input("Введите номер столбца: ") - 1
        print("\n")

        if self.__ground.update_arr(target_colomn, player): #если столбец полон, ход начнётся заново
            self.turn(cur_player)
        else:
            self.chang_turn(cur_player)

    def chang_turn(self, cur_player):
        if cur_player + 1 == len(self.__plaers):
            self.__currant_player = 0
        else:
            self.__currant_player += 1
        self.__turns_count += 1
        self.turn(self.__currant_player)


    def game_over(self, winner):
        self.__started = False
        if winner == "full ground":
            print("Ничья")
            exit()
        print(f"Победил {winner.name}")
        exit()

    def name_input(self, text=""):
        while True:
            try:
                a = input(text)
                if type(a) == str:
                    return a
                else:
                    print("Введите имя\n")
            except:
                print("Что-то не так...\n")

    def number_input(self, text=""):
        while True:
            try:
                a = int(input(text))
                if 1 <= a <= 9:
                    return a
                else:
                    print("от 1 до 9 включительно\n")
            except:
                print("Вветите число от 1 до 9\n")

    def turn_input(self, text=""):
        while True:
            try:
                a = int(input(text))
                if 0 < a <= self.__size:
                    return a
                else:
                    print(f"от 0 до {self.__size - 1} включительно\n")
            except:
                print("Что-то не так\n")

    @property
    def count_to_win(self):
        return self.__count_to_win

game = Game(6, 4)
game.start_game()