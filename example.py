import whatsapp_sender

# Example usage of the library functions

# To send a scheduled message (in 2 minutes from now)
# Replace with a valid phone number (include country code)
phone_number = "+1234567890"  # Example: Replace with your recipient's number (with country code)

# Get current time and add 2 minutes
import datetime
now = datetime.datetime.now()
hour = now.hour
minute = now.minute + 2

# Handle minute overflow
if minute >= 60:
    minute = 0
    hour += 1
if hour >= 24:
    hour = 0

print("Example 1: Sending a scheduled message")
whatsapp_sender.send_whatsapp_message(
    phone_number=phone_number,
    message="Hello! This is a scheduled test message.",
    hour=hour,
    minute=minute
)

# Uncomment to send an instant message
print("\nExample 2: Sending an instant message")
whatsapp_sender.send_whatsapp_message_instantly(
   phone_number=phone_number,
   message="Hello! This is an instant test message."
)

# Uncomment to send a message to a group
# Replace with a valid group ID from the group invite link
# group_id = "AB123CDEfghi456"  # Example: Replace with your group ID
# print("\nExample 3: Sending a message to a group")
# whatsapp_sender.send_whatsapp_to_group(
#    group_id=group_id,
#    message="Hello everyone! This is a test group message.",
#    hour=hour,
#    minute=minute
# )
