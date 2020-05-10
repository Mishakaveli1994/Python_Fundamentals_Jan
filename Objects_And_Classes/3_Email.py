'''Lab Solution'''
# class Email:
#     def __init__(self, sender, receiver, content, is_set='False'):
#         self.sender = sender
#         self.receiver = receiver
#         self.content = content
#         self.is_set = is_set
#
#     def send(self):
#         self.is_set = 'True'
#
#     def get_info(self):
#         return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_set}"
#
#
# emails = []
# while True:
#     command = input()
#     if command == 'Stop':
#         break
#     else:
#         command_split = command.split(' ')
#         sender = command_split[0]
#         receiver = command_split[1]
#         content = command_split[2]
#         email = Email(sender, receiver, content)
#         emails.append(email)
#
# send_email = list(map(lambda x: int(x), input().split(", ")))
# for x in send_email:
#     emails[x].send()
#
# for email in emails:
#     print(email.get_info())

'''Instructor Solution'''


class Person:
    def __init__(self, name):
        self.name = name


class Email:
    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.recipient}: {self.content}. Sent: {self.is_sent}"


class MailBox:
    def __init__(self):
        self.emails = []

    def add_email(self, email):
        self.emails.append(email)

    def send_emails(self, indexes):
        for i in indexes:
            self.emails[i].send()

    def get_all_mails_info(self):
        all_info = ''
        for email in self.emails:
            all_info += f"{email.get_info()}\n"
        return all_info


mailbox = MailBox()

while True:
    command = input()
    if command == 'Stop':
        break
    else:
        sender_name, recipient_name, content = command.split(' ', maxsplit=2)
        sender = Person(sender_name)
        recipient = Person(recipient_name)
        email = Email(sender_name, recipient_name, content)
        mailbox.add_email(email)
sent_indexes = [int(i.strip()) for i in input().split(',')]
mailbox.send_emails(sent_indexes)
print(mailbox.get_all_mails_info())