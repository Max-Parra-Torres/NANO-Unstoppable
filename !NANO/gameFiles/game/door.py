class Door:
    def __init__(self, code, locked=True):
        self.code = code
        self.locked = locked

    def unlock(self, attempt):
        if attempt == self.code:
            self.locked = False
            print("The door is unlocked!"
                  "Detective D!BZY: 'I got it! I can go into the tea house now.\n'")
            return True
        else:
            print("The lock doesn't budge.\n"
                  "Detective D!BZY: 'I should check for clues...'")
            return False

    def is_locked(self):
        return self.locked
