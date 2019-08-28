class ProductChoice:

    def __init__(self, name=None, link=None):
        self.name = name
        self.link = link

    def __eq__(self, other):
        return self.name == other.name \
               and (self.link is None or other.link is None or self.link == other.link)

    def __repr__(self):
        return "ProductChoice(%s, %s)" % (self.name, self.link)
