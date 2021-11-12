
# You are going to create a program that will help Ada track the sales from her game store. 
# Please do not use another tool, like Repl.it to complete this challenge. 
# Your code will not appropriately translate to the HackerRank environment.

# Requirements
# -	You must use at least one loop
# -	You must use at least one dictionary or list to store your data

# Problem Statement
# 1-	A single pack of trading cards id $4.25
# 2-	36 packs of trading cards are $125.00
# 3-	Dice are $11.00 per set
# 4-	Board games are $50.00
# 5-	The program should report each of the following:
# 1-	A summary of earnings for each customer.
# 2-	The total earnings for all customers.
# 3-	The total earned from non-trading card products(dice + board games)
# 4-	The most profitable customer.




def sales_summary(packs_purchased, dice_purchased, board_games_purchased):
    """
    Parameters:
      packs_purchased: How many packs of trading cards each customer purchased.
      dice_purchased: How many sets of dice were each customer purchased.
      board_games_purchased: How many board games each customer purchased.
    """
    print("Welcome to the Ada's Game Emporium Sales Tracker!")
    print()
    game_emporium = Game(packs_purchased, dice_purchased, board_games_purchased)
    game_emporium.report()
    

class Game:

    def __init__(self, packs_purchase, dice_purchase, board_games_purchase):
        self.packs_purchase = packs_purchase
        self.dice_purchase = dice_purchase
        self.board_games_purchase = board_games_purchase
        self.validate_inputs()

    def validate_inputs(self):
        all_inputs = zip(self.packs_purchase, self.dice_purchase, self.board_games_purchase)
        
        if not len(self.packs_purchase) == len(self.dice_purchase) == len(self.board_games_purchase):
            raise ValueError("Invalid input- customer order size must be equal")

        for pack, dice, board in all_inputs:
            if not isinstance(pack, int) or not isinstance(dice, int) or not isinstance(board, int):
                raise TypeError("Invalid input- input must be integer")
            if pack < 0 or dice < 0 or board < 0:
                raise Exception("Invalid input- all inputs must be positive integer")
        


    def packs_calculation(self, customer):
        return (self.packs_purchase[customer] // 36) * 125.00 + (self.packs_purchase[customer] % 36) * 4.25

    def dice_calculation(self, customer):
        return self.dice_purchase[customer] * 11.00

    def board_games_calculation(self, customer):
        return self.board_games_purchase[customer] * 50.00

    def earning_per_customer(self, customer):
        return self.packs_calculation(customer) + self.dice_calculation(customer) + self.board_games_calculation(customer)

    def total_earnings(self):
        total= 0
        for customer in range(len(self.packs_purchase)):
            total += self.earning_per_customer(customer)
        return total
    
    def total_non_tradings(self):
        total= 0 
        for customer in range(len(self.packs_purchase)):
            total += self.dice_calculation(customer) + self.board_games_calculation(customer)
        return total

    def most_profits(self):
        max = {}
        for customer in range(len(self.packs_purchase)):
            max[customer] = self.earning_per_customer(customer)
        return max

    def max_value(self):
        return max(self.most_profits().values())

    def profitable_customer(self):
        max_keys = [customer for customer, spent in self.most_profits().items() if spent == self.max_value()]
        #index starts from zero however ranks start from one and we are looking for rank here
        multiple_keys = [str(customer + 1) for customer in max_keys]
        return multiple_keys

    def format_price(self, price):
        return '{:.2f}'.format(price)

    def report(self):
        for customer in range(len(self.packs_purchase) ):
            print(f"Customer {str(customer + 1)} spent ${self.format_price(self.earning_per_customer(customer))}")
            print(f">>> ${self.format_price(self.packs_calculation(customer))} for trading card packs")
            print(f">>> ${self.format_price(self.dice_calculation(customer))} for dice sets")
            print(f">>> ${self.format_price(self.board_games_calculation(customer))} for board games")
            print()
        print(f"Combined all customers paid ${self.format_price(self.total_earnings())} total")
        print(f"Non-trading card products (dice + board games) were ${self.format_price(self.total_non_tradings())} total")
        print()
        print( f"${self.format_price(self.max_value())} was the most paid by any single customer")
        print("The customer(s) that paid the most were: #" + ', #'.join(self.profitable_customer()))


packs_purchased = [10, 5, 35] 
dice_purchased = [2, 0, 3]    
board_games_purchased = [3, 2, 0]  

sales_summary(packs_purchased, dice_purchased, board_games_purchased)
