from datetime import datetime as dt
class Hungry:
    def __init__(self, name, state):
        self.__state = state
        self.__name = name
    @property
    def name(self):
        return self.__name

hung_value = []
hung_value.append(Hungry("dead", 0))
hung_value.append(Hungry("very_hungry", 1))
hung_value.append(Hungry("hungry", 2))
hung_value.append(Hungry("normal", 3))
hung_value.append(Hungry("bit", 4))
hung_value.append(Hungry("overeat", 5))

class Mood:
    def __init__(self, name, state):
        self.__state = state
        self.__name = name
    @property
    def name(self):
        return self.__name

mood_value = []
mood_value.append(Hungry("escape", 0))
mood_value.append(Hungry("very_bad", 1))
mood_value.append(Hungry("sad", 2))
mood_value.append(Hungry("normal", 3))
mood_value.append(Hungry("good", 4))
mood_value.append(Hungry("happy", 5))

class Zver:
    """tamagoch"""
    def __init__(self, name, eat_timeout, play_timeout, hungry_stats, mood_stats):
        self.__name = name
        self.__eat_timeout = eat_timeout
        self.__hungry_stats = hungry_stats
        self.__mood_stats = mood_stats
        self.__play_timeout = play_timeout
        self.__st = dt.now()
        self.__already_ate = 0
        self.__already_played = 0

    def current_state(self):
        div_time = (dt.now() - self.__st).total_seconds()
        hung = int(self.__already_ate - (div_time // self.__eat_timeout) + 3)
        if hung <= 0 or hung > 5:
            print("It's dead")
            exit()
        else:
            self.__hungry_stats = hung

        mood = int(self.__already_played - div_time // self.__play_timeout + 3)
        if mood <= 0:
            print("It escaped")
            exit()
        elif (mood >= 5):
            self.__mood_stats = 5
        else:
            self.__mood_stats = mood

    def eat(self, amount):
            self.__already_ate += amount
            Zver.current_state(self)
            print("Current state: ", hung_value[self.__hungry_stats].name,"\n")

    def play(self):
        if self.__already_played <= 6:
            self.__already_played += 1
        Zver.current_state(self)
        print("Current state: ", mood_value[self.__mood_stats].name, "\n")

    def show(self):
        Zver.current_state(self)
        print("Name: ", self.__name, "\n"
              "Hungry: ", hung_value[self.__hungry_stats].name, "\n"
              "Mood: ", mood_value[self.__mood_stats].name, "\n"
              "Already ate: ", self.__already_ate, "\n"
              "Already played: ", self.__already_played, "\n")


zver = Zver("Dogy", 10, 10, 3, 3)


def Gameplay():
    print("Управление: \n"
          "1 - накормить \n"
          "2 - поиграть \n"
          "3 - показать инфо \n"
          "0 - выход \n")
    while True:
        try:
            a = int(input("Введи команду: "))
        except ValueError:
            print("Неверно, попробуйте ещё")
            continue
        if (a == 0 or a == 1 or a == 2 or a == 3) == False:
            print("Неверно, попробуйте ещё")
            continue
        if a == 0:
            exit()
        elif a == 1:
            b = 0
            while True:
                try:
                    b = int(input("Сколько порций (1 - 3): "))
                except ValueError:
                    print("Неверно, попробуйте ещё")
                    continue
                if b == 1 or b == 2 or b == 3:
                    break
                else:
                    print("Неверно, попробуйте ещё")
                    continue
            zver.eat(b)
        elif a == 2:
            zver.play()
        elif a == 3:
            zver.show()
Gameplay()