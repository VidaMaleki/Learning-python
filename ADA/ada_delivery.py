# Problem statement 
# 1- Single delivery is $7.25 (tips aren't tracked by th app).
# 2- 10 deliveries are $60.00 (a discounted rate).
# 3- "Rush delivery" is an additional $2.00 per delivery.
# 4- Meal cost $12.50 each(can have multiple meals per delivery).
# 5- The program should report each of the following

#     1- A summary of earnings for each customer
#         delivery_report + rush_report +  meal_report
        
#     2- The total earnings for all customers.
#         customer 1 + customer 2 + customer 3

#     3- The total earned from delivery fees(rush and standard delivery fees)delivery.
#         delivery_report + rush_report

#     4- The customer that spent the most.
#         a dictionary of spent per customer
#         most spent money(value)
#         most spent customer(key)


# example input: 
# deliveries_ordered
# 1
# 2
# 2
# rush_deliveries
# 1
# 0
# 2
# meals_purchased
# 3
# 2
# 4

# out puts
# Welcome to the Ada Meal Delivery Dashboard

# customer 1 paid $46.75 total
# >>> $7.25 in delivery fees
# >>> $2.00 in rush delivery fees
# >>> $37.50 in meal fees

# customer 2 paid $39.50 total
# >>> $14.50 in delivery fees
# >>> $0.00 in rush delivery fees
# >>> $25.00 in meal fees

# customer 3 paid $68.50 total
# >>> $14.50 in delivery fees
# >>> $4.00 in rush delivery fees
# >>> $50.00 in meal fees

# Combined all customers paid $    total
# Delivery fees (standard and Rush Delivery) were $
# $   was the most paid by any single customer
# The customer(s) that paid the most were: #
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
