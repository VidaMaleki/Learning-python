
def subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases):
    """
    Parameters:
      months_subscribed: How many months each account purchased.
      ad_free_months: How many months each account paid for ad free viewing.
      video_on_demand_purchases: How many Videos on Demand each account purchased.
    """
    print("Welcome to the Ada+ Account Dashboard")
    print()


class Subscription:

    def __init__(self):
        self.total_ad_frees = {}
        self.total_videos = {}
        self.total_months = {}


    def total_ad_free(self, number):
        ad_free_service = int(input("How many Ad free would you like to purchase? ")) 
        self.total_ad_frees[number] = ad_free_service * 2
        
    def total_video(self, number):
        video_on_demand = int(input("How many Video on Demand would you like to purchase? ")) 
        self.total_videos[number] =   video_on_demand * 27.99       

    def total_month(self, number):
        month_service = int(input("How many month would you like to purchase? "))
        self.total_months[number] = (month_service // 3 ) * 18 + (month_service % 3 ) * 7
 
    def report_total(self):
        print(self.total_ad_frees[i] + self.total_months[i] + self.total_videos[i])

    def report_total_Video_Adfree(self):
        print(self.total_ad_frees[i] + self.total_videos[i])

    def report_most_profitable(self, customer):
        
        print()

ad = Subscription()


for i in range(1, 4):
    print("Customer " + str(i) + ": " )
    ad.total_ad_free(i)
    ad.total_video(i)
    ad.total_month(i)

for i in range(1, 4):
    print("Purchase summary: \n")
    ad.report_total()
    ad.report_total_video()
    ad.report_total_ad_free()






    