import threading
import time
from factorial import factorial


def multithreading_test():
    """
    Perform factorial calculations using multithreading.
    Creates 3 threads for 50!, 100!, and 200!.
    Measures time over 10 rounds.
    """
    print("=" * 60)
    print("MULTITHREADING TEST")
    print("=" * 60)
    print("Calculating: 50!, 100!, 200! with 3 threads")
    print("Running 10 rounds...")
    print()

    def calculate_factorial(number, result_dict, key):
        """Helper function for thread execution"""
        start_time = time.perf_counter_ns()
        fact_result = factorial(number)
        end_time = time.perf_counter_ns()
        result_dict[key] = (start_time, end_time, fact_result)

    times = []  # Store times for each round

    for round_num in range(1, 11):
        # Dictionary to store thread results
        results = {}

        # Record start time before creating threads
        overall_start = time.perf_counter_ns()

        # Create and start threads
        thread1 = threading.Thread(target=calculate_factorial, args=(50, results, 'fact50'))
        thread2 = threading.Thread(target=calculate_factorial, args=(100, results, 'fact100'))
        thread3 = threading.Thread(target=calculate_factorial, args=(200, results, 'fact200'))

        thread1.start()
        thread2.start()
        thread3.start()

        # Wait for all threads to complete
        thread1.join()
        thread2.join()
        thread3.join()

        # Record end time after all threads finish
        overall_end = time.perf_counter_ns()

        # Calculate total elapsed time
        elapsed_time = overall_end - overall_start
        times.append(elapsed_time)

        print(f"Round {round_num}: {elapsed_time:,} ns")

    # Calculate average time
    avg_time = sum(times) / len(times)
    print(f"\nAverage Time (Multithreading): {avg_time:,.0f} ns")
    print(f"Average Time: {avg_time / 1000000:.2f} ms")

    return times


if __name__ == "__main__":
    multithreading_test()