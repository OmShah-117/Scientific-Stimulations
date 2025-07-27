import numpy as np
from datetime import datetime, timedelta
import pytz # For handling timezones accurately

def calculate_earth_elapsed_time(traveler_total_minutes):
    """
    Calculates the total elapsed time on Earth (in seconds) given a traveler's
    total minutes spent near a black hole, using a fixed time dilation model.

    Args:
        traveler_total_minutes (float): Total number of minutes the traveler
                                        experiences near the black hole.

    Returns:
        float: The total elapsed seconds on Earth.
        None: If an error occurs during time dilation calculation.
    """

    # --- 1. Define Constants and Black Hole Parameters ---
    c = 299792458  # Speed of light in m/s
    G = 6.674e-11  # Gravitational constant in N m^2/kg^2
    M_solar = 1.989e30  # Mass of one solar mass in kg

    # Mass of Sagittarius A* (approx 4.1 million solar masses)
    M_sgrA = 4.1e6 * M_solar  # in kg

    # Calculate Schwarzschild Radius (r_s) for Sagittarius A*
    r_s = (2 * G * M_sgrA) / (c**2)

    # --- 2. Assumed Values for the Traveler's Environment (from previous calculation) ---
    # These parameters determine the fixed time dilation factor for this specific scenario
    r_factor = 1.000000000001 # Distance from Sgr A* as a factor of r_s
    r = r_factor * r_s

    # The velocity 'v' was adjusted in the previous step to ensure a physically
    # valid discriminant (meaningful square root). This 'v' is relative to a
    # local stationary observer.
    grav_term_inner = (1 - (r_s / r))
    # Calculate the maximum possible local velocity for the formula to be real
    v_max_local = c * np.sqrt(grav_term_inner)
    v = 0.9999999999 * v_max_local # Set v just below the local limit

    # --- 3. Calculate the Combined Time Dilation Factor ---
    vel_term_inner = (v**2 / c**2)
    discriminant = grav_term_inner - vel_term_inner

    if discriminant <= 0:
        print("Error: The underlying time dilation parameters are too extreme or invalid for calculation.")
        return None
    
    time_dilation_factor = 1 / np.sqrt(discriminant)

    # --- 4. Calculate Elapsed Time on Earth ---
    traveler_seconds = traveler_total_minutes * 60 # Convert total minutes to seconds
    earth_elapsed_seconds = traveler_seconds * time_dilation_factor

    return earth_elapsed_seconds

# --- Main part of the script ---
if __name__ == "__main__":
    print("--- Black Hole Time Travel Calculator ---")
    print("This tool uses a fixed, extremely high time dilation")
    print("It assumes travel at extreme speed very close to Sagittarius A*.")
    print("-" * 40)

    # Define the starting point based on the prompt's context
    # We need to explicitly handle IST timezone. pytz.timezone('Asia/Kolkata')
    ist_tz = pytz.timezone('Asia/Kolkata')
    
    # Create a naive datetime object first
    start_time_naive = datetime(2025, 7, 23, 0, 12, 1) # Year, Month, Day, Hour, Minute, Second

    # Localize the naive datetime object to IST
    current_earth_time = ist_tz.localize(start_time_naive)

    print(f"Starting Earth Time: {current_earth_time.strftime('%A, %B %d, %Y %I:%M:%S %p %Z%z')}")
    print("-" * 40)

    try:
        user_input_days = float(input("Enter the number of days you (the traveler) spent near the black hole: "))
        user_input_minutes = float(input("Enter the number of minutes you (the traveler) spent near the black hole: "))

        if user_input_days < 0 or user_input_minutes < 0:
            print("Number of days and minutes cannot be negative. Please enter positive values.")
        else:
            traveler_total_minutes = (user_input_days * 24 * 60) + user_input_minutes
            earth_elapsed_seconds = calculate_earth_elapsed_time(traveler_total_minutes)

            if earth_elapsed_seconds is not None:
                # Convert elapsed seconds to more readable units (years, days, hours, minutes, seconds)
                elapsed_years = earth_elapsed_seconds / (365.25 * 24 * 60 * 60)
                remaining_seconds_after_years = earth_elapsed_seconds % (365.25 * 24 * 60 * 60)
                
                elapsed_days = remaining_seconds_after_years / (24 * 60 * 60)
                remaining_seconds_after_days = remaining_seconds_after_years % (24 * 60 * 60)
                
                elapsed_hours = remaining_seconds_after_days / (60 * 60)
                remaining_seconds_after_hours = remaining_seconds_after_days % (60 * 60)
                
                elapsed_minutes = remaining_seconds_after_hours / 60
                elapsed_seconds_final = remaining_seconds_after_hours % 60

                print("\n--- Time Travel Results ---")
                print(f"If you spent {user_input_days} day(s) and {user_input_minutes} minute(s) near the black hole, then on Earth:")
                
                # Check if the elapsed time is small enough for datetime object to handle
                # Arbitrary threshold, say less than 1000 years, to prevent OverflowError
                if elapsed_years < 1000:
                    try:
                        future_earth_time = current_earth_time + timedelta(seconds=earth_elapsed_seconds)
                        print(f"The exact date and time will be: {future_earth_time.strftime('%A, %B %d, %Y %I:%M:%S %p %Z%z')}")
                    except OverflowError:
                        print(f"The calculated time ({elapsed_years:.2f} years) is too far in the future for a precise calendar date.")
                        print(f"It would be approximately {int(elapsed_years)} years, {int(elapsed_days)} days, {int(elapsed_hours)} hours, {int(elapsed_minutes)} minutes, and {int(elapsed_seconds_final)} seconds from now.")
                        print(f"The year on Earth would be approximately: {current_earth_time.year + elapsed_years:.0f}")
                else:
                    print(f"The calculated time is extremely vast: {elapsed_years:.2e} years.")
                    print(f"The universe itself might have changed unrecognizably by then.")
                    print(f"It would be approximately {int(elapsed_years)} years, {int(elapsed_days)} days, {int(elapsed_hours)} hours, {int(elapsed_minutes)} minutes, and {int(elapsed_seconds_final)} seconds from now.")
                    print(f"The approximate year on Earth would be: {current_earth_time.year + elapsed_years:.0f}")

            else:
                print("Calculation aborted due to invalid physical parameters.")

    except ValueError:
        print("Invalid input. Please enter numbers for days and minutes.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
