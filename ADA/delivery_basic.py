def delivery_summary(deliveries_ordered, rush_deliveries, meals_purchased):
    """
    Parameters:
      deliveries_ordered: How many deliveries each customer ordered.
      rush_deliveries: How many deliveries each customer rushed.
      meals_purchased: How many total meals the customer purchased.
    """
    print("Welcome to the Ada Meal Delivery Dashboard")
    print()
    
    # Write your code here
    class Delivery:
    
        def __init__(self):
            self.deliveries = {}
            self.rush_orders = {}
            self.meals = {}
            self.total_earnings_per_customer = {}


        def deliveries_orders(self, i):
            self.deliveries[i] = (int(deliveries_ordered[i - 1]) // 10) * 60 + (int(deliveries_ordered[i - 1]) % 10) * 7.25
            return self.deliveries[i]

        def rush_delivery(self, i):
            self.rush_orders[i] = int(rush_deliveries[i - 1]) * 2
            return self.rush_orders[i]

        def meals_purchase(self, i):
            self.meals[i] = int(meals_purchased[i - 1]) * 12.50
            return self.meals[i]

        def total_earnings_per_customers(self, i):
            self.total_earnings_per_customer[i] = round(self.deliveries[i] + self.rush_orders[i] + self.meals[i], 2)
            return self.total_earnings_per_customer[i]

        def total_earnings(self):
            return sum(self.total_earnings_per_customer.values())

        def total_delivery_fees(self):
            return round(sum(list(self.deliveries.values()) + list(self.rush_orders.values())), 2)

        def most_spent_customer(self):
            m = max(self.total_earnings_per_customer.values())
            cusStr = ''
            for key, val in self.total_earnings_per_customer.items():
                if val == m:
                    cusStr += '#' + str(key) + ', '
            cusStr = cusStr[:-2]
            return cusStr
        
        def most_customer(self):
            return max(self.total_earnings_per_customer.values())

    ada = Delivery()
    num_customer = deliveries_ordered

    for i in range(1, len(deliveries_ordered) + 1):
        ada.deliveries_orders(i)
        ada.rush_delivery(i)
        ada.meals_purchase(i)
        print("Customer " + str(i) + " paid $" + str('{:.2f}'.format(ada.total_earnings_per_customers(i))) + " total")
        print(">>> $" + str('{:.2f}'.format(ada.deliveries_orders(i))) + " in delivery fees")
        print(">>> $" + str('{:.2f}'.format(ada.rush_delivery(i))) + " in rush delivery fees")
        print(">>> $" + str('{:.2f}'.format(ada.meals_purchase(i))) + " in meal fees\n")

    print("Combined all customers paid $" + str(ada.total_earnings()) + " total")
    print("Delivery fees (standard and Rush Delivery) were $" + str(ada.total_delivery_fees()) + " total\n")
    print("$" + str('{:.2f}'.format(ada.most_customer())) + " was the most paid by any single customer")
    print("The customer(s) that paid the most were: " + str(ada.most_spent_customer()))

deliveries_ordered = []
rush_deliveries = []
meals_purchased = []
num_customer = 3

for i in range(1, 4):
    print('Enter deliveries_ordered: ' + str(i))
    deliveries_ordered.append(input())
    print('Enter rush_deliveries: ' + str(i))
    rush_deliveries.append(input())
    print('Enter meals_purchased: ' + str(i))
    meals_purchased.append(input())

delivery_summary(deliveries_ordered, rush_deliveries, meals_purchased)   