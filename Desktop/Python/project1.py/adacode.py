

class Subscription:

    def __init__(self):
        self.total_ad_frees = {}
        self.total_videos = {}
        self.total_months = {}
        self.report_totals = {}

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
        self.report_totals[i] = round(self.total_ad_frees[i] + self.total_months[i] + self.total_videos[i] , 2)
        print("Total for all customers: ",round(self.total_ad_frees[i] + self.total_months[i] + self.total_videos[i] , 2))

    def report_total_Video_Adfree(self):
        print("Total 'Ad free' and 'Video On Demand' is: ", self.total_ad_frees[i] + self.total_videos[i])

    def report_most_profitable(self):
        print("The most profitable customer was: " + "Customer " + str(max(self.report_totals, key=self.report_totals.get)))
        

ada = Subscription()


for i in range(1, 4):
    print("Customer " + str(i) + ": " )
    ada.total_ad_free(i)
    ada.total_video(i)
    ada.total_month(i)
    #print("Total is: ")
    #ada.report_total(i)


print("\n Purchase summary: \n")
ada.report_total()
ada.report_total_Video_Adfree()
ada.report_most_profitable()





    