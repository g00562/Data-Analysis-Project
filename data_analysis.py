import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("Student.csv")

print("Dataset:")
print(data)

avg = data["Total_marks"].mean()
highest = data["Total_marks"].max()
lowest = data["Total_marks"].min()

print("\nAnalysis:")
print("Average Marks:", avg)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

plt.bar(data["Student_Name"],data["Total_marks"], color='skyblue', edgecolor='black', linewidth=1.5)
plt.xlabel("Students")
plt.xticks(rotation=45)
plt.ylabel("Marks")
plt.title("Student Marks Analysis")
plt.show()