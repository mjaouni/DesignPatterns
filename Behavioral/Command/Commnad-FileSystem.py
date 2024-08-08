from abc import ABC, abstractmethod

import shutil
import os


# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# Concrete Command Classes
class CopyCommand(Command):
    def __init__(self, file_system, src, dest):
        self.file_system = file_system
        self.src = src
        self.dest = dest

    def execute(self):
        self.file_system.copy(self.src, self.dest)

    def undo(self):
        self.file_system.delete(self.dest)


class MoveCommand(Command):
    def __init__(self, file_system, src, dest):
        self.file_system = file_system
        self.src = src
        self.dest = dest

    def execute(self):
        self.file_system.move(self.src, self.dest)

    def undo(self):
        self.file_system.move(self.dest, self.src)


class DeleteCommand(Command):
    def __init__(self, file_system, path):
        self.file_system = file_system
        self.path = path

    def execute(self):
        self.file_system.delete(self.path)

    def undo(self):
        print(f"Undo of delete operation is not supported for {self.path}")


# Receiver Class
class FileSystem:
    def copy(self, src, dest):
        shutil.copy(src, dest)
        print(f'Copied file from {src} to {dest}')

    def move(self, src, dest):
        shutil.move(src, dest)
        print(f'Moved file from {src} to {dest}')

    def delete(self, path):
        if os.path.exists(path):
            os.remove(path)
            print(f'Deleted file {path}')
        else:
            print(f'File {path} does not exist, cannot delete')


# Invoker Class
class FileManager:
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


# Usage
file_system = FileSystem()
file_manager = FileManager()

# Set up file paths
src = 'test_file.txt'
copy_dest = 'copied_test_file.txt'
move_dest = 'moved_test_file.txt'

# Create a test file
with open(src, 'w') as f:
    f.write("This is a test file.")

copy_command = CopyCommand(file_system, src, copy_dest)
move_command = MoveCommand(file_system, src, move_dest)
delete_command = DeleteCommand(file_system, copy_dest)

file_manager.execute_command(copy_command)
file_manager.execute_command(move_command)
file_manager.execute_command(delete_command)

file_manager.undo()
file_manager.undo()
file_manager.undo()
