from ada_delivery import Delivery

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
        
deliveries_ordered = [3, 5, 3] 
rush_deliveries = [1, 0, 2]    
meals_purchased = [3, 2, 3]  

delivery_summary(deliveries_ordered, rush_deliveries, meals_purchased)