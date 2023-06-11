import time

def stopwatch():
    print("Press ENTER to start the stopwatch")
    input()
    start_time = time.time()
    print("Stopwatch started. Press ENTER to stop.")
    input()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")

# Example usage:
stopwatch()


