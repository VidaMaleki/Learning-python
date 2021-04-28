

class Subscription:

    def __init__(self):
        self.total_ad_frees = {}
        self.total_videos = {}
        self.total_months = {}
        self.report_customer_total = {}
        self.report_total_ad_free = 0
        self.report_totals = 0

    def total_ad_free(self, number):
        ad_free_service = int(input("How many Ad free would you like to purchase? ")) 
        self.total_ad_frees[number] = ad_free_service * 2
        
    def total_video(self, number):
        video_on_demand = int(input("How many Video on Demand would you like to purchase? ")) 
        self.total_videos[number] =   video_on_demand * 27.99       

    def total_month(self, number):
        month_service = int(input("How many month would you like to purchase? "))
        self.total_months[number] = (month_service // 3 ) * 18 + (month_service % 3 ) * 7
 
    def report_total(self, customer):
        for i in range(1, customer + 1):
            self.report_totals += round(self.total_ad_frees[i] + self.total_months[i] + self.total_videos[i], 2)
            self.report_customer_total[i] = round(self.total_ad_frees[i] + self.total_months[i] + self.total_videos[i], 2)
        return self.report_totals

    def report_total_video_adfree(self, customer):
        for i in range(1, customer + 1):
            self.report_total_ad_free += round(self.total_ad_frees[i] + self.total_videos[i], 2)
        return self.report_total_ad_free

    def report_most_profitable(self):
        return max(self.report_customer_total, key=self.report_customer_total.get)
        

ada = Subscription()

num_customers = 3


for i in range(1, num_customers + 1):
    print("Customer " + str(i) + ": " )
    ada.total_ad_free(i)
    ada.total_video(i)
    ada.total_month(i)
    

print("\n Purchase summary: \n")
print("Total for all customers: " + str(ada.report_total(num_customers)))
print("Total 'Ad free' and 'Video On Demand' is: " + str(ada.report_total_video_adfree(num_customers)))
print("The most profitable customer was: " + "Customer " + str(ada.report_most_profitable()))





    