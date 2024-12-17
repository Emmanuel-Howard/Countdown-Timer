# Countdown Timer: Counting down from a user-provided input to 0
import time

def get_start_time():
    # Prompts the user to input a start time in seconds
    # Mitigates ValueError
    while True:
        start_time = input("How many seconds would you like to count down from?: ")
        try:
            start_time = int(start_time)
            return start_time
        except ValueError:
            print("Please input a valid number of seconds! ")

def countdown(seconds):
    # Counts down from the provided start time
    # Waits 1 second after each second printed
    for seconds in reversed(range(1, seconds + 1)):
        print(f"There are {seconds} seconds remaining...")
        time.sleep(1)
    print("Time's Up!")

def main():
    # Main function handles the project flow
    start_time = get_start_time()
    countdown(start_time)

if __name__ == "__main__":
    main()