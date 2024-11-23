# Read the times for each triathlon event
swimming_time = float(input("Enter the time taken for swimming (in minutes): "))
cycling_time = float(input("Enter the time taken for cycling (in minutes): "))
running_time = float(input("Enter the time taken for running (in minutes): "))

# Calculate the total time
total_time = swimming_time + cycling_time + running_time

# Determine the award based on the total time
if total_time <= 100:
    award = "Honorary Colours"
elif total_time <= 105:
    award = "Honorary Half Colours"
elif total_time <= 110:
    award = "Honorary Scroll"
else:
    award = "No award"

# Display the total time and the award
print(f"The total time taken to complete the triathlon is: {total_time:.2f} minutes")
print(f"The participant will receive: {award}")
