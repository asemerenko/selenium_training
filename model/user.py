class User:

    def __init__(self, email=None, password=None, firstname=None, lastname=None):
        self.email = email
        self.password = password
        self.firstname = firstname
        self.lastname = lastname

    def __eq__(self, other):
        return self.email == other.email and \
               (self.password is None or other.password is None or self.password == other.password) and \
               (self.firstname is None or other.firstname is None or self.firstname == other.firstname) and \
               (self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def __repr__(self):
        return "User(email: %s, password: %s, firstname: %s, lastname: %s)" % \
               (self.email, self.password, self.firstname, self.lastname)
