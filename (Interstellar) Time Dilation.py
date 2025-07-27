from datetime import datetime, timedelta
import pytz # For handling timezones accurately

def calculate_interstellar_time_dilation(traveler_hours, traveler_minutes):
    """
    Calculates the elapsed time on Earth based on the Interstellar movie's
    time dilation ratio (1 hour on Miller's Planet = 7 years on Earth).

    Args:
        traveler_hours (float): Number of whole hours the traveler experiences.
        traveler_minutes (float): Number of minutes the traveler experiences (can be fractional).

    Returns:
        float: The total elapsed seconds on Earth.
    """

    # Interstellar's = 1 hour on Miller's Planet = 7 years on Earth
    # folm= (Earth seconds) / (Traveler seconds)
    # Calculation: (7 years * 365.25 days/year * 24 hours/day * 60 min/hour * 60 sec/min) / (1 hour * 60 min/hour * 60 sec/min)
    interstellar_dilation_factor = (7 * 365.25 * 24 * 60 * 60) / (1 * 60 * 60)

    # Converted total traveler time to seconds
    total_traveler_seconds = (traveler_hours * 60 * 60) + (traveler_minutes * 60)
    
    earth_elapsed_seconds = total_traveler_seconds * interstellar_dilation_factor

    return earth_elapsed_seconds

def format_duration(seconds):
    """
    Formats a duration in seconds into human-readable units (years, days, hours, minutes, seconds).
    Chooses the largest relevant unit for the primary display.
    """
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    
    minutes = seconds / 60
    if minutes < 60:
        return f"{int(minutes)} minutes and {int(seconds % 60)} seconds"
        
    hours = minutes / 60
    if hours < 24:
        return f"{int(hours)} hours, {int(minutes % 60)} minutes, and {int(seconds % 60)} seconds"
        
    days = hours / 24
    if days < 365.25:
        return f"{int(days)} days, {int(hours % 24)} hours, {int(minutes % 60)} minutes, and {int(seconds % 60)} seconds"
        
    years = days / 365.25
    remaining_seconds_after_years = seconds % (365.25 * 24 * 60 * 60)
    
    remaining_days = remaining_seconds_after_years / (24 * 60 * 60)
    remaining_hours = (remaining_seconds_after_years % (24 * 60 * 60)) / (60 * 60)
    remaining_minutes = (remaining_seconds_after_years % (60 * 60)) / 60
    remaining_seconds = remaining_seconds_after_years % 60

    return (f"{int(years)} years, {int(remaining_days)} days, "
            f"{int(remaining_hours)} hours, {int(remaining_minutes)} minutes, "
            f"and {int(remaining_seconds)} seconds")


# --- Main part of the script ---
if __name__ == "__main__":
    print("--- Interstellar Time Dilation Calculator ---")
    print("Time dilation From movie Interstellar:")
    print("1 hour on 'Miller's Planet' = 7 years on Earth.")
    print("-" * 50)

    #  India.
    ist_tz = pytz.timezone('Asia/Kolkata')
    
    # naive datetime object 
    start_time_naive = datetime(2025, 7, 22, 14, 43, 0) # Year, Month, Day, Hour (24-hr), Minute, Second

    # naive datetime object to IST
    current_earth_time = ist_tz.localize(start_time_naive)

    print(f"Starting Earth Time (Solapur): {current_earth_time.strftime('%A, %B %d, %Y %I:%M:%S %p %Z%z')}")
    print("-" * 50)

    try:
        user_input_hours = float(input("Enter the number of whole hours you (the traveler) spent on 'Miller's Planet': "))
        user_input_minutes = float(input("Enter the number of minutes (can be fractional) you spent on 'Miller's Planet': "))
        
        if user_input_hours < 0 or user_input_minutes < 0:
            print("Hours and minutes cannot be negative. Please enter positive values.")
        else:
            earth_elapsed_seconds = calculate_interstellar_time_dilation(user_input_hours, user_input_minutes)

            if earth_elapsed_seconds is not None:
                # human-readable formatted duration
                formatted_duration = format_duration(earth_elapsed_seconds)
                
                print("\n--- Time Travel Results ---")
                print(f"If you spent {user_input_hours} hour(s) and {user_input_minutes} minute(s) on 'Miller's Planet', then on Earth:")
                print(f"A total of {formatted_duration} would have passed.")
                
                # Check if the elapsed time is small enough for datetime object to handle
                elapsed_years = earth_elapsed_seconds / (365.25 * 24 * 60 * 60)
                
                if elapsed_years < 1000: # Arbitrary threshold for datetime object
                    try:
                        future_earth_time = current_earth_time + timedelta(seconds=earth_elapsed_seconds)
                        print(f"The exact date and time would be: {future_earth_time.strftime('%A, %B %d, %Y %I:%M:%S %p %Z%z')}")
                    except OverflowError:
                        # Fallback for when it's just over the datetime limit
                        print(f"The exact calendar date is too far in the future for precise calculation.")
                        print(f"The approximate year on Earth would be: {current_earth_time.year + elapsed_years:.0f}")
                else:
                    # For extremely large numbers of years, just show the scientific notation
                    print(f"The exact calendar date is too far in the future for precise calculation.")
                    print(f"The approximate year on Earth would be: {current_earth_time.year + elapsed_years:.0f}")
                    print(f"Note: This is an extremely vast amount of time ({elapsed_years:.2e} years). The universe itself might have changed unrecognizably by then.")

            else:
                print("An error occurred during time dilation calculation.")

    except ValueError:
        print("Invalid input. Please enter numbers for hours and minutes.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
