# Handler Base Class
class PurchaseApprovalHandler:
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, amount):
        if self._next_handler:
            return self._next_handler.handle(amount)
        else:
            return print("Purchase Can't be approved")


# Concrete Handlers
class TeamLeader(PurchaseApprovalHandler):
    def handle(self, amount):
        if amount <= 1000:
            return f'Team Leader approved the purchase request of {amount} dollars '
        else:
            return super().handle(amount)


class DepartmentManager(PurchaseApprovalHandler):
    def handle(self, amount):
        if amount <= 5000:
            return f'Department Manager approved the purchase request of {amount} dollars '
        else:
            return super().handle(amount)


class CEO(PurchaseApprovalHandler):
    def handle(self, amount):
        if amount <= 20000:
            return f'CEO approved the purchase request of {amount} dollars '
        else:
            return super().handle(amount)


# Usage
# Create handlers
team_leader = TeamLeader()
department_manager = DepartmentManager()
ceo = CEO()

# Chain them together
team_leader.set_next(department_manager).set_next(ceo)

purchase_amount = [500, 2000, 7000, 15000, 25000]

for amount in purchase_amount:
    print(team_leader.handle(amount))
