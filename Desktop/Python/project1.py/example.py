#C14 Coding Challenge: Ada State Fair
#In this portion of the application, you will complete a short coding challenge based on the Ada Developers› Academy JumpStart Curriculum.
#What we’ re looking
#for
#Ability to self - learn and apply material quickly because as a professional engineer you will be learning every day, forever.
#Ability to grasp the fundamentals of coding so that you are ready
#for Day 1 of Ada.All admitted students are expected to be well - versed with the conditional flows, loops, arrays, hashes and Ruby fundamentals on the first day of their cohort.These concepts are covered in our Jump Start curriculum.
#Ability to describe code you have written, including how control flows through the program, what you tried, why you tried it, what worked and what didn’ t.
#Tools
#For this challenge, you will use this online REPL tool.If you are not sure where to get started, take a look at this lecture video that has REPL instructions and an introduction to programming concepts.The notes that go with the video are located here.
#Assignment: Ada State Fair
#You are going to create a program that will help the state of Ada track the amount earned through ticket and food sales
#Requirements
#You must accept user input through gets.chomp.
#You must use at least one loop or iterator.
#You must use at least one Hash or Array to store your data.
#Problem Statement
#A single ticket is $35 .00
#Tickets can be purchased in lots of 4
#for $112 .00
#Cotton candy is sold
#for $1 .25 per serving.
#Curly fries are sold
#for $2 .50
#for a small and $4 .00
#for a large.
#The program should read in 3 parties’ ticket purchases and food purchases.
#The program should then report each of the following.
#A summary
#for each party.
#The total earnings
#for the session.
#The total spent on concessions.
#The most expensive party.*/

amount_earned_tickets_sales = 0
amount_earned_foods_sales = 0
tickets = ['single_ticket', 'group_tickets']
single_ticket = 35.00
group_ticket_4 = 112.00


foods = ['cotton_candy_per serving', 'Small_curly_fries', 'Large_curly_fries']
cotton_candy = 1.25
small_curly_fries = 2.50
large_curly_fries = 4.00

party_numbers = 3

party_purchases = tickets + foods



ticket_purchases = 0
food_purchases = 0
The_total_earning = 0
The_total_spent_on_concessions = 0
The_most_expensive_party = 0