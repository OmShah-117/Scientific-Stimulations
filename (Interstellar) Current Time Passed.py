from datetime import datetime, timedelta

# Define the movie release date
movie_release_date = datetime(2013, 1, 1)

# Define the current date based on execution time
current_date = datetime.now() #actual current time when executed
# For this example, I use the specific time from the context:
current_date = datetime(2025, 7, 27, 14, 54, 43)

# Calculate Earth years passed dynamically
time_difference = current_date - movie_release_date
total_days_passed = time_difference.days
earth_years_passed_dynamic = total_days_passed / 365.25

# Interstellar time dilation ratio
interstellar_ratio_years_per_hour = 4

# Calculate time passed on Miller's Planet dynamically
miller_planet_hours_dynamic = earth_years_passed_dynamic / interstellar_ratio_years_per_hour

# Convert to hours, minutes, and seconds
hours_comp = int(miller_planet_hours_dynamic)
remaining_minutes_float = (miller_planet_hours_dynamic - hours_comp) * 60
minutes_comp = int(remaining_minutes_float)
remaining_seconds_float = (remaining_minutes_float - minutes_comp) * 60
seconds_comp = int(remaining_seconds_float)

print(f"Time passed on Earth from movie release to now: {earth_years_passed_dynamic:.2f} years")
print(f"Corresponding time passed on 'Miller's Planet': {hours_comp} hour(s), {minutes_comp} minute(s), and {seconds_comp} second(s).")
