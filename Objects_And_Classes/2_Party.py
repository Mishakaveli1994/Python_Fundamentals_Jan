class Party:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def get_summary(self):
        return f"Going: {', '.join(self.people)}\nTotal: {len(self.people)}"


party = Party()
line = input()
while line != 'End':
    party.add_person(line)
    line = input()

print(party.get_summary())
