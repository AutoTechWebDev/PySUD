# Define the dungeon map and rooms
dungeon_map = {
     'start_room': Room(description="You are in the entrance of the dungeon...",
                        exits={'north': 'hallway'}),
     'hallway': Room(description="A dimly lit hallway...",
                     exits={'south': 'start_room', 'east': 'treasure_room'},
                     items=['key']),
     'treasure_room': Room(description="A room filled with treasure...",
                          exits={'west': 'hallway'},
                          items=['treasure_chest']),
        }