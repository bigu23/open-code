import time
import winsound

def focus_timer(work_minutes, break_minutes, rounds):
    for i in range(rounds):
        print(f"Round {i + 1}/{rounds}: Work for {work_minutes} minutes.")
        time.sleep(work_minutes * 60)  # Convert minutes to seconds
        winsound.Beep(440, 1000)  # Beep to notify the end of work time
        print("Time's up! Take a break.")
        time.sleep(break_minutes * 60)  # Convert minutes to seconds
        winsound.Beep(880, 1000)  # Beep to notify the end of break time
        print("Break's over. Back to work!")

if __name__ == "__main__":
    work_minutes = int(input("Enter work time in minutes: "))
    break_minutes = int(input("Enter break time in minutes: "))
    rounds = int(input("Enter number of rounds: "))

    focus_timer(work_minutes, break_minutes, rounds)
# open-code
