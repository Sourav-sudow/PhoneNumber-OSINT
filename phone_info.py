import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def phone_info(number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(number)

        # Validate if the number is possible
        if not phonenumbers.is_possible_number(parsed_number):
            print("❌ Invalid phone number. Not a possible number.")
            return

        # Validate if the number is valid
        if not phonenumbers.is_valid_number(parsed_number):
            print("❌ Invalid phone number. Not a valid number.")
            return

        # Get country & region
        country = geocoder.description_for_number(parsed_number, "en") or "Unknown"

        # Get carrier info
        sim_operator = carrier.name_for_number(parsed_number, "en") or "Unknown"

        # Get time zone
        time_zones = timezone.time_zones_for_number(parsed_number)
        time_zone_str = ", ".join(time_zones) if time_zones else "Unknown"

        print("\n📞 Phone Number Information:")
        print(f"🌍 Country: {country}")
        print(f"📡 Carrier: {sim_operator}")
        print(f"⏰ Time Zone: {time_zone_str}")
    
    except phonenumbers.phonenumberutil.NumberParseException:
        print("❌ Invalid phone number format. Please enter a correct one.")
    except Exception as e:
        print(f"⚠ Error Occurred: {e}")

# Get user input
if __name__ == "__main__":
    phone_number = input("🔍 Enter phone number (with country code, e.g., +91XXXXXXXXXX): ")
    phone_info(phone_number)
