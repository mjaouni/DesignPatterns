# Handler Base Class
class SupportHandler:
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, issue_type):
        if self._next_handler:
            return self._next_handler.handle(issue_type)
        else:
            return "Issue Can't Be resolved."


# Concrete Handlers
class FirstLevelSupport(SupportHandler):
    def handle(self, issue_type):
        if issue_type == 'Password Reset':
            return 'First Level Support resolves the Password Reset issue'
        else:
            return super().handle(issue_type)


class SecondLevelSupport(SupportHandler):
    def handle(self, issue_type):
        if issue_type == 'Software Installation':
            return 'Second Level Support resolves Software Installation issue'
        else:
            return super().handle(issue_type)


class ThirdLevelSupport(SupportHandler):
    def handle(self, issue_type):
        if issue_type == 'Network Issue':
            return 'Third Level Support resolves Network Issue'
        else:
            return super().handle(issue_type)


# Usage
first_level_support = FirstLevelSupport()
second_level_support = SecondLevelSupport()
third_level_support = ThirdLevelSupport()

first_level_support.set_next(second_level_support).set_next(third_level_support)

issue_types = ['Password Reset','Software Installation','Network Issue','Hardware Failure']

for issue in issue_types:
    print(first_level_support.handle(issue))