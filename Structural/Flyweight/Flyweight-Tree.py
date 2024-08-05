# Intrinsic State
class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x, y):
        print(
            f'Drawing the tree with name {self.name} with color {self.color} and texture {self.texture} at position ({x},{y})')


#  Flyweight Factory
class TreeFactory:
    _tree_types = {}

    @classmethod
    def get_tree_type(cls, name, color, texture):
        if name not in cls._tree_types:
            cls._tree_types[name] = TreeType(name, color, texture)
        return cls._tree_types[name]


# Tree class represents the context, which includes the extrinsic state (e.g., coordinates)
class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self):
        self.tree_type.draw(self.x, self.y)


# Use the Flyweight
class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, name, color, texture):
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self):
        for tree in self.trees:
            tree.draw()


# Usage
forest = Forest()
forest.plant_tree(1, 1, 'Oak', 'Green', 'Rough')
forest.plant_tree(2, 2, 'Pine', 'Green', 'Smooth')
forest.plant_tree(3, 3, 'Oak', 'Green', 'Rough')
forest.plant_tree(4, 4, "Pine", "Green", "Smooth")

forest.draw()