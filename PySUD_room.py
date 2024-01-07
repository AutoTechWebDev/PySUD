# ROOM INFORMATION BELOW HERE
class Room:
    def room(self, description, exits, items=None, monster=None):
        self.description = description
        self.exits = exits
        self.items = items if items else []
        self.monster = monster