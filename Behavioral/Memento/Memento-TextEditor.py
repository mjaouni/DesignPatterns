# Memento
from typing import Any


class Memento:
    def __init__(self, state: str):
        self._state = state

    def get_state(self) -> str:
        return self._state


# Originator
class TextEditor:
    def __init__(self):
        self._text = ""

    def type(self, words: str):
        self._text += words

    def get_content(self) -> str:
        return self._text

    def save(self) -> Memento:
        return Memento(self._text)

    def restore(self, memento: Memento):
        self._text = memento.get_state()


# Caretaker
class EditorHistory:
    def __init__(self):
        self._history = []

    def push(self, memento: Memento):
        self._history.append(memento)

    def pop(self) -> Memento | None:
        if self._history:
            return self._history.pop()
        return None


# Usage

editor = TextEditor()
history = EditorHistory()

editor.type('Hello ')
history.push(editor.save())
editor.type('World! ')
history.push(editor.save())

editor.type("This is a test")
print(f"Current Content:'{editor.get_content()}'")

editor.restore(history.pop())
print(f'After Undo : "{editor.get_content()}"')

editor.restore(history.pop())
print(f'After Undo : "{editor.get_content()}"')
