import copy
from abc import ABC, abstractmethod


# Abstract Prototype
class Document:
    def __init__(self, title, content, footer):
        self.title = title
        self.content = content
        self.footer = footer

    @abstractmethod
    def clone(self):
        pass

    def __str__(self):
        return f'Document title:{self.title},Content:{self.content},Footer:{self.footer}'


# Report:Concrete of Document
class Report(Document):
    def __init__(self, title, content, footer, author, date):
        super().__init__(title, content, footer)
        self.author = author
        self.date = date

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return (f'Report(title={self.title}, content={self.content}, footer={self.footer}, '
                f'author={self.author}, date={self.date})')


# Report:Concrete of Letter
class Letter(Document):
    def __init__(self, title, content, footer, sender, recipient):
        super().__init__(title, content, footer)
        self.sender = sender
        self.recipient = recipient

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return (f'Letter(title={self.title}, content={self.content}, footer={self.footer}, '
                f'sender={self.sender}, recipient={self.recipient})')


# Usage
original_report = Report(
    title='Annual Financial Report',
    content='This is the financial report for the year 2024.',
    footer='Confidential',
    author='Finance Department',
    date='2024-07-01'
)

original_letter = Letter(
    title="Welcome Letter",
    content="Welcome to our company. We are excited to have you!",
    footer="Best regards, HR Team",
    sender="HR Department",
    recipient="New Employee"
)

cloned_report = original_report.clone()
cloned_letter = original_letter.clone()

# Modify the cloned documents
cloned_report.title = "Quarterly Financial Report"
cloned_report.date = "2024-07-29"

cloned_letter.recipient = "John Doe"
cloned_letter.content = "Dear John Doe, Welcome to our company. We are thrilled to have you on board!"

# Display the original and cloned documents
print(original_report)
# Output: Report(title=Annual Financial Report, content=This is the financial report for the year 2024.,
# footer=Confidential, author=Finance Department, date=2024-07-01)

print(cloned_report)
# Output: Report(title=Quarterly Financial Report, content=This is the financial report for the year 2024.,
# footer=Confidential, author=Finance Department, date=2024-07-29)

print(original_letter)
# Output: Letter(title=Welcome Letter, content=Welcome to our company. We are excited to have you!, footer=Best
# regards, HR Team, sender=HR Department, recipient=New Employee)

print(cloned_letter)
# Output: Letter(title=Welcome Letter, content=Dear John Doe, Welcome to our company. We are thrilled to have you on
# board!, footer=Best regards, HR Team, sender=HR Department, recipient=John Doe)
