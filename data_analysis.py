import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("/Users/mac/Desktop/Data-Analysis/Student.csv")

print("Dataset:")
print(data)

avg = data["Total_marks"].mean()
highest = data["Total_marks"].max()
lowest = data["Total_marks"].min()

print("\nAnalysis:")
print("Average Marks:", avg)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

plt.bar(data["Student_Name"],data["Total_marks"], )
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Analysis")
plt.show()