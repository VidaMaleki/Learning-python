
def subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases):
    """
    Parameters:
      months_subscribed: How many months each account purchased.
      ad_free_months: How many months each account paid for ad free viewing.
      video_on_demand_purchases: How many Videos on Demand each account purchased.
    """
    print("Welcome to the Ada+ Account Dashboard")
    print()


service_type = ['Months', 'Video_on_Demand', 'Ad_Free']
service_value = [7.00, 27.99, 2.00, 18.00]

class A:

    def __init__(self, name, values):
        self.name = name
        self.values = values

    def customer_number(self, num_customer):
        
        customers = []
        for i in range(num_customer):
            current_customer = "Customer: " + str(i + 1) 
            customers.append(current_customer)
        return customers



    def calculate_bill(self, purchased_items):
        bill = 0
        for purchased_item in purchased_items:
            if purchased_item in self.values:
                bill += self.values[purchased_item]
        return bill

print(A.customer_number(0, 3))



