import random

class Coin:
    def __init__(self, x_range, y_range, obstacles, bot_position):
        self.x = None
        self.y = None
        self.x_range = x_range
        self.y_range = y_range
        self.obstacles = obstacles
        self.bot_position = bot_position
        self.positions = set()
        self.create_coins()

    def create_coins(self):
        while len(self.positions) < self.x_range[1] * self.y_range[1]:
            x, y = self.generate_random_position()
            self.positions.add((x, y))

    def generate_random_position(self):
        while True:
            # Random x, y position for the coin
            x = random.randint(self.x_range[0], self.x_range[1])
            y = random.randint(self.y_range[0], self.y_range[1])

            # Check if the coin is not on an obstacle
            if (x, y) not in self.obstacles:

                # Check if the coin is not on the bot
                if (x, y) != self.bot_position and (x, y) not in self.positions:
                    # Add the new coin position to the set of positions
                    self.positions.add((x, y))
                    # Return the valid coin position
                    return x, y

    def __str__(self):
        return f"Coins positions: {self.positions}"


# Define the main function
def main():
    # Set up the game parameters
    x_range = (0, 10)
    y_range = (0, 10)
    obstacles = [(2, 2), (3, 5), (7, 8)]
    bot_position = (5, 5)

    # Create a Coin object and print its positions
    coins = Coin(x_range, y_range, obstacles, bot_position)
    print(coins)


# Call the main function
if __name__ == "__main__":
    main()
