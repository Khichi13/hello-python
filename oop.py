""" Object-Oriented Programming in Python. """


class Train:
    def __init__(self, name): # constructors
        self.name = name
        self.destroyed = False

    def explode(self):
        print('BOOOM!')
        self.destroyed = True
    
    def run(self):
        if not self.destroyed:
            print('Running...')
        else:
            print(':(')