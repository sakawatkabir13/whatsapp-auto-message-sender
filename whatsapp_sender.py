
import pywhatkit
import datetime
import time
import sys

def send_whatsapp_message(phone_number, message, hour=None, minute=None, wait_time=15, close_tab=True):
    """
    Send a WhatsApp message to a specific phone number.
    
    Parameters:
        phone_number (str): Phone number with country code but without any + or spaces
        message (str): Message to be sent
        hour (int, optional): Hour of the day to send the message (24-hour format). Defaults to current hour.
        minute (int, optional): Minute of the hour to send the message. Defaults to current minute + 1.
        wait_time (int, optional): Time to wait in seconds before sending the message. Defaults to 15.
        close_tab (bool, optional): Whether to close the tab after sending the message. Defaults to True.
    """
    # Ensure the phone number has the country code prefix with +
    if not phone_number.startswith('+'):
        phone_number = '+' + phone_number
    # If time is not specified, use current time + 1 minute
    if hour is None or minute is None:
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute + 1
        # Handle minute overflow
        if minute >= 60:
            minute = 0
            hour += 1
        if hour >= 24:
            hour = 0
    
    try:
        print(f"Preparing to send message to {phone_number} at {hour}:{minute}")
        print("Make sure WhatsApp is linked to WhatsApp Web!")
        
        # Send the WhatsApp message
        pywhatkit.sendwhatmsg(phone_number, message, hour, minute, wait_time, close_tab)
        print("Message sent successfully!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def send_whatsapp_message_instantly(phone_number, message, close_tab=True):
    """
    Send a WhatsApp message instantly without scheduling.
    
    Parameters:
        phone_number (str): Phone number with country code but without any + or spaces
        message (str): Message to be sent
        close_tab (bool, optional): Whether to close the tab after sending the message. Defaults to True.
    """
    # Ensure the phone number has the country code prefix with +
    if not phone_number.startswith('+'):
        phone_number = '+' + phone_number
    try:
        print(f"Sending instant message to {phone_number}")
        print("Make sure WhatsApp is linked to WhatsApp Web!")
        
        # Send the WhatsApp message instantly
        pywhatkit.sendwhatmsg_instantly(phone_number, message, wait_time=15, tab_close=close_tab)
        print("Message sent successfully!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def send_whatsapp_to_group(group_id, message, hour=None, minute=None, wait_time=15, close_tab=True):
    """
    Send a WhatsApp message to a group.
    
    Parameters:
        group_id (str): Group ID from the group's invite link
        message (str): Message to be sent
        hour (int, optional): Hour of the day to send the message (24-hour format). Defaults to current hour.
        minute (int, optional): Minute of the hour to send the message. Defaults to current minute + 1.
        wait_time (int, optional): Time to wait in seconds before sending the message. Defaults to 15.
        close_tab (bool, optional): Whether to close the tab after sending the message. Defaults to True.
    """
    # Group ID doesn't need a + prefix as it's not a phone number
    # If time is not specified, use current time + 1 minute
    if hour is None or minute is None:
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute + 1
        # Handle minute overflow
        if minute >= 60:
            minute = 0
            hour += 1
        if hour >= 24:
            hour = 0
    
    try:
        print(f"Preparing to send message to group {group_id} at {hour}:{minute}")
        print("Make sure WhatsApp is linked to WhatsApp Web!")
        
        # Send the WhatsApp message to the group
        pywhatkit.sendwhatmsg_to_group(group_id, message, hour, minute, wait_time, close_tab)
        print("Message sent successfully!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    print("WhatsApp Auto Message Sender")
    print("===========================")
    
    if len(sys.argv) < 3:
        print("Usage examples:")
        print("  For individual (scheduled in 1 min): python whatsapp_sender.py individual +1234567890 'Hello, this is an automated message'")
        print("  For individual (custom time): python whatsapp_sender.py individual +1234567890 'Hello, message at custom time' 14 30")
        print("  For instant message: python whatsapp_sender.py instant +1234567890 'Hello, urgent message!'")
        print("  For group: python whatsapp_sender.py group 'AB123CDEfghi456' 'Hello group, this is an automated message'")
        print("  For group (custom time): python whatsapp_sender.py group 'AB123CDEfghi456' 'Hello group, custom time' 15 45")
        sys.exit(1)
        
    message_type = sys.argv[1].lower()
    recipient = sys.argv[2]
    message = sys.argv[3]
    
    # Check if custom time parameters are provided
    hour = None
    minute = None
    if len(sys.argv) >= 6:
        try:
            hour = int(sys.argv[4])
            minute = int(sys.argv[5])
            # Validate time values
            if not (0 <= hour <= 23 and 0 <= minute <= 59):
                print("Error: Hour must be between 0-23 and minute between 0-59")
                sys.exit(1)
        except ValueError:
            print("Error: Time parameters must be valid numbers")
            sys.exit(1)
    
    if message_type == "individual":
        send_whatsapp_message(recipient, message, hour, minute)
    elif message_type == "instant":
        send_whatsapp_message_instantly(recipient, message)
    elif message_type == "group":
        send_whatsapp_to_group(recipient, message, hour, minute)
    else:
        print(f"Unknown message type: {message_type}")
        print("Supported types: individual, instant, group")
        sys.exit(1)
