import matplotlib.pyplot as plt
import numpy as np
# Basic Line Plot
# x = [1,2,3,4,5]
# y = [1,4,9,16,25]

# plt.plot(x,y,linestyle='--',marker='o',linewidth=3,markersize=5)
# plt.xlabel("numbers")
# plt.ylabel("squares")
# plt.title("number VS squares")
# plt.show()



# Problem 1: Daily Temperature

# A weather station recorded the temperature in Lahore over one week:

# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# temps = [31, 33, 35, 38, 36, 32, 30]

# Plot temperature vs day. Then answer:

# Which day was the hottest? The coolest?
# Between which two consecutive days did temperature rise the fastest?
# What is the overall trend across the week?






# Problem 2: Mobile Phone Battery

# A phone's battery percentage was checked every hour:

# hours = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# battery = [100, 92, 85, 76, 60, 55, 38, 20, 5]

# Plot battery vs hours. Then answer:

# During which hour did the battery drain the most?
# Roughly how much battery is used per hour on average?
# If the pattern continues, when will the phone die?


# Problem 3: Shop Sales

# A juice shop tracked how many glasses it sold each month:

# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]
# sales = [120, 135, 160, 210, 290, 350, 340, 310]

# Plot sales vs month. Then answer:

# In which month did sales peak? Why might that be? (Hint: think weather)
# Which month had the biggest jump in sales compared to the previous month?





# Problem 4: Student Study Hours vs Test Score

# A student recorded weekly study hours and their weekly quiz score:

# python
# weeks = [1, 2, 3, 4, 5, 6, 7, 8]
# study_hours = [2, 3, 3, 5, 6, 4, 7, 8]
# scores = [55, 60, 58, 70, 78, 65, 85, 90]

# Plot both study_hours and scores on the same graph (two lines, use plt.legend()). Then answer:

# Do the two lines move together? What does that suggest?
# In week 6 the student studied less — what happened to the score?
# Predict the score if the student studies 9 hours.


# plt.plot(weeks,scores,label="week vs score")
# plt.plot(weeks,study_hours,label="week vs study hourse")
# plt.xlabel("Week")
# plt.ylabel("value")
# plt.title("Study hours VS Quiz Scores")
# plt.legend()
# plt.show()


# Problem 5: Population Growth

# The population of a small town (in thousands):

# years = [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025]
# population = [12, 14, 17, 22, 30, 41, 55, 74]

# Plot population vs year. Then answer:

# Is the population growing at a constant rate, or speeding up? How can you tell from the shape of the line?
# Roughly how many years did it take for the population to double from 12,000?
# Estimate the population in 2030 if the pattern continues.


# data = [1,2,2,2,3,3,3,3,3,3,4,4,5,5,5,5,5,5]
# plt.hist(data,bins=5,color='green',edgecolor='black')
# plt.show()

x = [1,2,3,4,5,6,7]
y = [1,4,9,16,25,36,49]

plt.scatter(x,y,color='blue',marker='x')
a,b,c = np.polyfit(x,y,2)
plt.plot(x,a*np.array([n**2 for n in x])+b*np.array(x)+c,color='red')
plt.show()