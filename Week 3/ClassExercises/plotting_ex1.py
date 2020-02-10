
import matplotlib.pyplot as plt

# 1) create a line graph showing attendance over time. hint: use keys() and values() method of the dictionary.
# 2) add title and labels for x and y axis.

student_attendance = {'day1': 33, 'day2': 34, 'day3': 29,
                      'day4': 31, 'day5': 28, 'day6': 26, 'day7': 30}

plt.figure()

plt.plot(list(student_attendance.keys()),
         list(student_attendance.values()), linewidth=5)

# Set chart title and label axes.
plt.title("Student Attendance", fontsize=24)
plt.xlabel("Day", fontsize=14)
plt.ylabel("Attendance count", fontsize=14)
# Set size of tick labels.

plt.tick_params(axis='both', labelsize=14)
plt.show()
