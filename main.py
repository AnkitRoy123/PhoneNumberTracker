
from phonenumbers import *

def track_number(number):
    try:
        # Parse the number (assumes international format like +14155552671)
        parsed_number = phonenumbers.parse(number)

        # Get country/region
        country = geocoder.description_for_number(parsed_number, "en")

        # Get carrier name
        sim_carrier = carrier.name_for_number(parsed_number, "en")

        # Get timezone(s)
        timezones = timezone.time_zones_for_number(parsed_number)

        print(f"\n[Phone Number Info]")
        print(f"Number: {number}")
        print(f"Region: {country}")
        print(f"Carrier: {sim_carrier}")
        print(f"Timezone(s): {', '.join(timezones)}")
    
    except phonenumbers.NumberParseException:
        print("Invalid phone number format.")

# Example usage
number_input = input("Enter phone number with country code (e.g., +14155552671): ")
track_number(number_input)
