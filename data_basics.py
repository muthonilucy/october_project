import pandas as pd
import matplotlib.pyplot as plt


# reading the school.csv data by creating a variable called data and using the function read_csv()
data = pd.read_csv('school.csv')

# print(data.head())    # first 5 rows

# print(data.tail())    # last five rows

# print(data['bday'])   # print a column

# print(data['English'])    # print 2 columns

# print(data.describe())    # summarizes the data into min, max, percentiles, std etc

# print(data.size)  # number of cells

# print(data.shape) # rows and columns

# print(data[0:4])    # slicing

# print(data[-11:])   # last 10 rows

# print(data['Math'].mean())  # mean of column

# print(data.isnull().sum())  # number of empty cells per columns

# data['Gender'].fillna(2, inplace=True)   # fills blank values eg gender with a value as 2
# print(data.isnull().sum())  # gender is filled

# data.to_csv("new_data.csv")  # save new values into new data file

# data['Gender'].replace(0, "Male", inplace=True)
# data['Gender'].replace(1, "Female", inplace=True)
# data['Gender'].replace(2, "Gender Neutral", inplace=True)
#
# data.to_excel("new_file2.xlsx")

# clean data to remove blanks and replace with mean value
mean_math = data["Math"].mean()
mean_english = data["English"].mean()
mean_reading = data["Reading"].mean()

data["Math"].fillna(mean_math, inplace=True)
data["English"].fillna(mean_english, inplace=True)
data["Reading"].fillna(mean_reading, inplace=True)



# Histogram
# graph, ax = plt.subplots()
# ax.hist(data["Math"], color='blue')
# ax.set_title("Math Distribution")
# ax.set_xlabel("Math")
# ax.set_ylabel("Frequency")
# plt.show()

# scatter chart
# graph, ax = plt.subplots()
# ax.scatter(data["Math"], data["English"], color='blue')
# ax.set_title("Scatter Chart")
# ax.set_xlabel("Math")
# ax.set_ylabel("Frequency")
# plt.show()

# pie chart example
labels = 'English', 'Math', 'Reading'
sizes = [data['English'].mean(), data['Math'].mean(), data['Reading'].mean()]
colors = ['blue', 'red', 'gold']

#plot
plt.pie(sizes,labels = labels, colors = colors)
plt.axis('equal')
plt.show()


