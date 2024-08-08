# Handler Base Class
class DocumentHandler:
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler: 'DocumentHandler'):
        self._next_handler = handler
        return handler

    def handle(self, document_type):
        if self._next_handler:
            return self._next_handler.handle(document_type)
        else:
            return "Document approval request can't be handled"


# Concrete Handlers
class Supervisor(DocumentHandler):
    def handle(self, document_type):
        if document_type == "Leave Request":
            return 'Supervisor approved the Leave Request'
        else:
            return super().handle(document_type)


class Manager(DocumentHandler):
    def handle(self, document_type):
        if document_type == "Expense Report":
            return 'Manager approved the Expense Report'
        else:
            return super().handle(document_type)


class Director(DocumentHandler):
    def handle(self, document_type):
        if document_type == "Project Proposal":
            return 'Director approved the Project Proposal'
        else:
            return super().handle(document_type)


class Test:
    def __init__(self):
        print('Test')


# Usage
supervisor = Supervisor()
manager = Manager()
director = Director()

supervisor.set_next(manager).set_next(director)

document_types = ['Leave Request', 'Expense Report', 'Project Proposal', 'Employment Contract']

for document_type in document_types:
    print(supervisor.handle(document_type))
