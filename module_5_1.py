class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(f'Этаж {floor}')
        else:
            print("Такого этажа не существует")


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)



#2 вариант чисто от себя на пробу как это будет работать в томже лифте,
#class House:
#    def __init__(self, name, number_of_floors):
#        self.name = name
#       self.number_of_floors = number_of_floors

#    def go_to(self):
#        try:
#            new_floor = int(input("Введите номер этажа: "))
#            if 1 <= new_floor <= self.number_of_floors:
#                for floor in range(1, new_floor + 1):
#                    print(f'Этаж {floor}')
#                print(f"Вы приехали на {new_floor}-й этаж.")
#            else:
#                print("Такого этажа не существует")
#        except ValueError:
#            print("Ошибка: введите целое число")


#h1 = House('ЖК Горский', 18)
#h2 = House('Домик в деревне', 2)

#h1.go_to()
#h2.go_to()
