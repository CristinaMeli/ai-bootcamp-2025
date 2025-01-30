class Directory:
    def __init__(self):
        self.contacts = []

    def add(self, contact):
        self.contacts.append(contact)

    def __len__(self):
        return len(self.contacts)

    def query(self, name):
        return [contact for contact in self.contacts if contact.name == name]

    def find(self, term):
        results = []
        for contact in self.contacts:
            if term in contact.name or \
                    (contact.phone and term in contact.phone) or \
                    (contact.surname and term in contact.surname):
                results.append(contact)
        return results

class Person(Directory):
    def __init__(self, name, phone = None, surname = None):
        self.name = name
        self.phone = phone
        self.surname = surname
        self.type = "Person"

class Business(Directory):
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.surname = None
        self.type = "Business"

directory = Directory()

directory.add(Person(name= "Margaret",surname="Hamilton", phone="01-234-567"))
directory.add(Business(name="Vedrai", phone="+39-333-333333"))
directory.add(Person(name="Linda", surname="Hamilton"))
