import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.base_attack_power = 20

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self):
        player_name = input("Введите имя вашего героя: ")
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def attack(self, attacker, defender):
        # Генерируем случайный урон в диапазоне от 0.8 до 1.2 от базовой силы удара
        damage = int(attacker.base_attack_power * random.uniform(0.8, 1.2))

        # Вероятность критического удара (20%)
        if random.random() < 0.2:
            damage *= 2
            print(f"Критический удар!")

        defender.health -= damage
        print(f"{attacker.name} атакует {defender.name} и наносит {damage} урона!")

    def player_turn(self):
        print(f"\nЗдоровье {self.player.name}: {self.player.health}")
        print(f"Здоровье {self.computer.name}: {self.computer.health}")
        self.attack(self.player, self.computer)

    def computer_turn(self):
        print(f"\nХод компьютера...")
        self.attack(self.computer, self.player)

    def declare_winner(self):
        if self.player.is_alive():
            print(f"\nПоздравляем! {self.player.name} победил!")
        else:
            print(f"\nУвы, {self.computer.name} победил!")

    def start(self):
        print("\nИгра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player_turn()
            if not self.computer.is_alive():
                break

            # Ход компьютера
            self.computer_turn()

        self.declare_winner()


def main():
    game = Game()
    game.start()


if __name__ == "__main__":
    main()