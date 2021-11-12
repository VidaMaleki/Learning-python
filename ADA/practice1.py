def subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases):
    """
    Parameters:
     months_subscribed:
     ad_free_months:
     video_on_demand_purchases:
    """
    print('Welcome to the Ada+ Account Dashboard')
    total_earnings_per_customer = []
    most_profitable_customer = []
    ad_free_months_total_earnings = 0
    video_on_demand_purchases_total_earning = 0
    total_earnings = 0
    most = "The accounts that earned the most were: "
    for x in range(len(months_subscribed)):
        monthly_subscription_earning = (int(months_subscribed[x]) // 3) * 18 + (int(months_subscribed[x]) % 3) * 7
        ad_free_months_earning = int(ad_free_months[x]) * 2
        video_on_demand_purchases_earning = int(video_on_demand_purchases[x]) * 27.99

        total_earnings_per_customer.append(monthly_subscription_earning + ad_free_months_earning + video_on_demand_purchases_earning)
        ad_free_months_total_earnings += ad_free_months_earning
        video_on_demand_purchases_total_earning += video_on_demand_purchases_earning

        most_profitable_customer.append(total_earnings_per_customer[x])

        total_earnings += total_earnings_per_customer[x]
        
        #monthly_subscription_earning
        print("\nAccount " + str(x + 1) + " made $" + str('{:.2f}'.format(total_earnings_per_customer[x]) + " total"))
        print(">>> $" + str('{:.2f}'.format(monthly_subscription_earning)) + " from montly subscription fees")
        print(">>> $" + str('{:.2f}'.format(ad_free_months_earning)) + " from Ad-free upgrades")
        print(">>> $" + str('{:.2f}'.format(video_on_demand_purchases_earning)) + " from Video on Demand purchases")
    
    ma = max(most_profitable_customer)
    maxList = [i + 1 for i, j in enumerate(most_profitable_customer) if j == ma]
    for i in maxList:
        most += "#" + str(i) + ", "
    most = most[:-2]

    print("\nCombined all accounts made $" + str('{:.2f}'.format(total_earnings)) + " total")
    print("Premium content (Ad-free watching and Video on Demand) made $" + str('{:.2f}'.format(ad_free_months_total_earnings + video_on_demand_purchases_total_earning)) + " total")
    print("\n$" + str('{:.2f}'.format(ma)) + " was the most earned by any single account")
    print(most)


monthly_fee = 7
ad_free_monthly_fee = 9
video_on_demand_price = 27.99
customer_months_subscribed = []
customer_ad_free_months_subscribed = []
customer_video_on_demand_purchases = []

for x in range(3):
    print('Enter months subscribed for customer ' + str(x))
    customer_months_subscribed.append(input())
    print('Enter ad free months subscribed for customer ' + str(x))
    customer_ad_free_months_subscribed.append(input())
    print('Enter video on demand purchases for customer ' + str(x))
    customer_video_on_demand_purchases.append(input())

subscription_summary(customer_months_subscribed, customer_ad_free_months_subscribed, customer_video_on_demand_purchases)
