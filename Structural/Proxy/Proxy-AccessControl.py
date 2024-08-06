from abc import ABC, abstractmethod


class File(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, content):
        pass

    @abstractmethod
    def delete(self):
        pass


# Class RealFile
class RealFile(File):
    def __init__(self, filename):
        self.filename = filename
        self.content = ""

    def read(self):
        print(f'Read file {self.filename}: {self.content} ')

    def write(self, content):
        self.content = content
        print(f'Writing to file {self.filename}: {self.content} ')

    def delete(self):
        print(f'Deleting {self.filename}')
        self.content = ""


# Class ProtectedProxyFile

class ProtectedProxyFile:
    def __init__(self, filename, user_role):
        self.real_file = RealFile(filename)
        self.user_role = user_role

    def read(self):
        self.real_file.read()

    def write(self, content):
        if self.user_role in ['admin', 'editor']:
            self.real_file.write(content)
        else:
            print(f"Access denied. User with role {self.user_role} can't write to the file")

    def delete(self):
        if self.user_role == 'admin':
            self.real_file.delete()
        else:
            print(f"Access denied. User with role {self.user_role} can't delete the file")


# Usage

user_role_guest = 'guest'
user_role_editor = 'editor'
user_role_admin = 'admin'

guest_file = ProtectedProxyFile('guest_file.txt', user_role_guest)
guest_file.read()
guest_file.write('Guest writing to the file')
guest_file.delete()

editor_file = ProtectedProxyFile('editor_file.txt',user_role_editor)
editor_file.read()
editor_file.write('Editor writing to the file')
editor_file.delete()
editor_file.read()

admin_file = ProtectedProxyFile('admin_file.txt',user_role_admin)
admin_file.read()
admin_file.write('Admin writing to the file')
admin_file.read()
admin_file.delete()