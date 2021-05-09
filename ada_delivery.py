def delivery_summary(deliveries_ordered, rush_deliveries, meals_purchased):
    """
    Parameters:
      deliveries_ordered: How many deliveries each customer ordered.
      rush_deliveries: How many deliveries each customer rushed.
      meals_purchased: How many total meals the customer purchased.
    """
    print("Welcome to the Ada Meal Delivery Dashboard")
    print()
    delivery = Delivery(deliveries_ordered, rush_deliveries, meals_purchased) 
    delivery.report()





class Delivery:

    def __init__(self, delivery_orders, rush_orders, meal_orders): 
        if len(delivery_orders) != len(rush_orders) or len(delivery_orders) !=len(meal_orders):
            raise Exception("invalid input- customer order size must be equal")  
        for customer_id in range(len(delivery_orders)):
            if delivery_orders[customer_id] < 0 or rush_orders[customer_id] < 0 or meal_orders[customer_id] < 0:
                raise Exception("Invalid input- input must be positive")

        self.delivery_orders = delivery_orders
        self.rush_orders = rush_orders
        self.meal_orders = meal_orders  

    def delivery_report(self, customer_id):
        return (self.delivery_orders[customer_id] // 10) * 60.00 + (self.delivery_orders[customer_id] % 10) * 7.25 
        
    def rush_report(self, customer_id):
        return self.rush_orders[customer_id] * 2.00

    def meals_report(self, customer_id):
        return self.meal_orders[customer_id] * 12.50

    def total_earning_per_customer(self, customer_id):
        return self.delivery_report(customer_id) + self.rush_report(customer_id) + self.meals_report(customer_id)
        
    def total_earnings(self):
        total= 0
        for customer_id in range(len(self.delivery_orders)):
           total += self.total_earning_per_customer(customer_id)
        return total

    def total_delivery_fees(self):
        total = 0
        for customer_id in range(len(self.delivery_orders)):
            total += self.delivery_report(customer_id) + self.rush_report(customer_id)
        return total

    def spent_by_customers(self):
        cost_by_customers_dictionary = {}
        for customer_id in range(len(self.delivery_orders)):
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
        for customer_id in range(len(self.delivery_orders) ):
            print("Customer " + str(customer_id + 1) + " paid $" + self.format_price(self.total_earning_per_customer(customer_id)) + " total")
            print(">>> $" + self.format_price(self.delivery_report(customer_id)) + " in delivery fees")
            print(">>> $" + self.format_price(self.rush_report(customer_id)) + " in rush delivery fees")
            print(">>> $" + self.format_price(self.meals_report(customer_id)) + " in meal fees")
            print()
        print("Combined all customers paid $" + str(self.total_earnings()) + " total")
        print("Delivery fees (standard and Rush Delivery) were $" + self.format_price(self.total_delivery_fees()) + " total")
        print()
        print( "$" + str('{:.2f}'.format(self.most_spent())) + " was the most paid by any single customer")
        print("The customer(s) that paid the most were: #" + ', #'.join(self.most_spent_customers()))


deliveries_ordered = [3, 5, 3] 
rush_deliveries = [1, 0, 2]    
meals_purchased = [3, 2, 3]  

delivery_summary(deliveries_ordered, rush_deliveries, meals_purchased)