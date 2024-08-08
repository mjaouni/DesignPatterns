from abc import ABC, abstractmethod


# Command Interface
class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# Concrete Command Classes
class WriteCommand(Command):
    def __init__(self, receiver, text):
        self.receiver = receiver
        self.text = text

    def execute(self):
        self.receiver.write(self.text)

    def undo(self):
        self.receiver.undo_write(self.text)


class PrintCommand(Command):
    def __init__(self, receiver, text):
        self.receiver = receiver
        self.text = text

    def execute(self):
        self.receiver.print(self.text)

    def undo(self):
        self.receiver.undo_print(self.text)


# Receiver Class
class Document:

    def __init__(self):
        self.content = ""

    def write(self, text):
        self.content += text
        print(f'Document Content {self.content}')

    def undo_write(self, text):
        self.content = self.content[:-len(text)]
        print(f'Document Content after undo {self.content}')


class Printer:

    def __init__(self):
        self.content = ""

    def print(self, text):
        self.content += text
        print(f'Printing Content {self.content}')

    def undo_print(self, text):
        self.content = self.content[:-len(text)]
        print(f'Printing Content after undo {self.content}')


# Invoker Class
class TextEditor:
    def __init__(self):
        self.commands = []
        self.current_command = 0

    def execute_command(self, command):
        self.commands = self.commands[:self.current_command]
        self.commands.append(command)
        command.execute()
        self.current_command += 1

    def undo(self):
        if self.current_command > 0:
            self.current_command -= 1
            self.commands[self.current_command].undo()

    def redo(self):
        if self.current_command < len(self.commands):
            self.commands[self.current_command].execute()
            self.current_command += 1


# Client Code
document = Document()
text_editor = TextEditor()

# Creating Commands
write_hello = WriteCommand(document, "Hello")
write_world = WriteCommand(document, "World")

# Executing commands
text_editor.execute_command(write_hello)
text_editor.execute_command(write_world)

text_editor.undo()
text_editor.undo()

text_editor.redo()
text_editor.redo()


printer = Printer()

# Creating Print Commands
print_hello = PrintCommand(printer, "Hi")
print_world = PrintCommand(printer, "World")

text_editor.execute_command(print_hello)
text_editor.execute_command(print_world)

text_editor.undo()
text_editor.undo()

text_editor.redo()
text_editor.redo()
