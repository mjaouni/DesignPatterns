# Memento
class PlayerMemento:
    def __init__(self, position, health, inventory):
        self._position = position
        self._health = health
        self._inventory = inventory

    def get_state(self):
        return self._position, self._health, self._inventory


# Originator
class Player:
    def __init__(self):
        self._position = (0, 0)
        self._health = 100
        self._inventory = []

    def move(self, x, y):
        self._position = (self._position[0] + x, self._position[1] + y)
        print(f'Player moved to {self._position}')

    def take_damage(self, amount):
        self._health = max(0, self._health - amount)
        print(f'Player took {amount} damage.Health is now {self._health}')

    def pick_item(self, item):
        self._inventory.append(item)
        print(f'Player picked up {item}.Inventory:{self._inventory}')

    def save(self) -> PlayerMemento:
        return PlayerMemento(self._position, self._health, self._inventory[:])

    def restore(self, memento: PlayerMemento):
        self._position, self._health, self._inventory = memento.get_state()
        print(f'Player restored to position {self._position} ,health {self._health}, inventory {self._inventory}')

    def get_status(self):
        print(f'Positions:{self._position},Health:{self._health},Inventory:{self._inventory}')


# Caretaker
class GameHistory:
    def __init__(self):
        self._history = []

    def save(self, memento: PlayerMemento):
        self._history.append(memento)

    def undo(self) -> PlayerMemento | None:
        if self._history:
            return self._history.pop()
        return None


# Usage

player = Player()
history = GameHistory()

player.move(5, 0)
player.pick_item('Sword')
player.get_status()
history.save(player.save())

player.move(0, 10)
player.take_damage(30)
player.pick_item('Shield')
player.get_status()
history.save(player.save())

player.move(-3,5)
player.take_damage(50)
player.get_status()


# Undo last action
player.restore(history.undo())
player.get_status()

# Undo another action
player.restore(history.undo())
player.get_status()