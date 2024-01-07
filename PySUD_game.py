# GENERAL GAME INFORMATION BELOW HERE
class Game:
    def game_over(self):
            # Define your game over conditions here
            # Example: Player wins if they reach a certain room
            if self.current_room.name == 'final_room':
                print("Congratulations! You've found the magical artifact. You win!")
                return True

            # Example: Player loses if health reaches zero
            if self.health <= 0:
                print("Game Over! Your health reached zero. Try again.")
                return True

            # Add more game over conditions as needed

            return False  # If none of the game over conditions are met  