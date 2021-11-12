#!/bin/python3


#
# Complete the 'sales_summary' function below.
#

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
    # Write your code here


class Game:
    def __init__(self, packs_purchase, dice_purchased, board_game_purchased): 
        if len(packs_purchase) != len(dice_purchased) or len(packs_purchase) !=len(board_game_purchased):
            raise Exception("invalid input- customer order size must be equal")  
        for customer_id in range(len(packs_purchase)):
            if packs_purchase[customer_id] < 0 or dice_purchased[customer_id] < 0 or board_game_purchased[customer_id] < 0:
                raise Exception("Invalid input- input must be positive")
            if not isinstance(packs_purchase[customer_id], int) or not isinstance(dice_purchased[customer_id], int) or not isinstance(board_game_purchased[customer_id], int):
                raise TypeError("Invalid input- please check input must be integer")
        self.packs_purchase = packs_purchase
        self.dice_purchased = dice_purchased
        self.board_game_purchased = board_game_purchased  

    def packs_report(self, customer_id):
        return (self.packs_purchase[customer_id] // 36) * 125.00 + (self.packs_purchase[customer_id] % 36) * 4.25 
        
    def dice_report(self, customer_id):
        return self.dice_purchased[customer_id] * 11.00

    def board_game_report(self, customer_id):
        return self.board_game_purchased[customer_id] * 50.00

    def total_earning_per_customer(self, customer_id):
        return self.packs_report(customer_id) + self.dice_report(customer_id) + self.board_game_report(customer_id)
        
    def total_earnings(self):
        total= 0
        for customer_id in range(len(self.packs_purchase)):
           total += self.total_earning_per_customer(customer_id)
        return total

    def total_non_tradings(self):
        total = 0
        for customer_id in range(len(self.packs_purchase)):
            total += self.board_game_report(customer_id) + self.dice_report(customer_id)
        return total

    def spent_by_customers(self):
        cost_by_customers_dictionary = {}
        for customer_id in range(len(self.packs_purchase)):
           cost_by_customers_dictionary[customer_id] = self.total_earning_per_customer(customer_id)
        return cost_by_customers_dictionary

    def most_spent(self):
        return max(self.spent_by_customers().values())
    
    def most_spent_customers(self):
        max_keys = [k for k, v in self.spent_by_customers().items() if v == self.most_spent()]
        multiple_keys = [str(k + 1) for k in max_keys]
        return multiple_keys
    
    def format_price(self, price):
        return '{:.2f}'.format(price)

    def report(self):
        for customer_id in range(len(self.packs_purchase) ):
            print(f"Customer {str(customer_id + 1)} spent ${self.format_price(self.total_earning_per_customer(customer_id))}")
            print(f">>> ${self.format_price(self.packs_report(customer_id))} for trading card packs")
            print(f">>> ${self.format_price(self.dice_report(customer_id))} for dice sets")
            print(f">>> ${self.format_price(self.board_game_report(customer_id))} for board games")
            print()
        print(f"Combined all customers paid ${self.format_price(self.total_earnings())} total")
        print(f"Non-trading card products (dice + board games) were ${self.format_price(self.total_non_tradings())} total")
        print()
        print( f"${self.format_price(self.most_spent())} was the most paid by any single customer")
        print("The customer(s) that paid the most were: #" + ', #'.join(self.most_spent_customers()))
    

            

packs_purchased = [2, 1, 1] 
dice_purchased = [1, 3, 2]    
board_games_purchased = [1, 3, 2]  

sales_summary(packs_purchased, dice_purchased, board_games_purchased)