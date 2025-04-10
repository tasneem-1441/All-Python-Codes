
import time
def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)  # Simulating a delay
print("Starting single-threaded execution")
print_numbers()
print("Execution finished")