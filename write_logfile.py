from datetime import datetime

def log_user_activity():
    
    # Asks a message and appends it to log.txt with a timestamp.

    print("Simple Logger Program")
    print("Type your message/activity and press Enter. Type 'exit' to quit.")

    while True:
        # Get user input
        user_input = input("Enter activity: ")
        
        # Exit program
        if user_input.lower() == 'exit':
            print("Exiting program.")
            break

        # Get the current timestamp and format it
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Create the log file entry
        log_entry = f"[{timestamp}] {user_input}\n"

        # Write the log entry to the file in append mode ('a')
        try:
            with open("log.txt", "a") as log_file:
                log_file.write(log_entry)
            print(f"Logged: {user_input}")
        except IOError as e:
            print(f"Error writing to file: {e}")

if __name__ == "__main__":
    log_user_activity()
