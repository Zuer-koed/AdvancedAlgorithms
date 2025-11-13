import time
from factorial import factorial


def non_multithreading_test():
    """
    Perform factorial calculations without multithreading.
    Calculates 50!, 100!, and 200! sequentially.
    Measures time over 10 rounds.
    """
    print("=" * 60)
    print("NON-MULTITHREADING TEST")
    print("=" * 60)
    print("Calculating: 50!, 100!, 200! sequentially")
    print("Running 10 rounds...")
    print()

    times = []  # Store times for each round

    for round_num in range(1, 11):
        # Record start time
        start_time = time.perf_counter_ns()

        # Calculate factorials sequentially
        fact50 = factorial(50)
        fact100 = factorial(100)
        fact200 = factorial(200)

        # Record end time
        end_time = time.perf_counter_ns()

        # Calculate elapsed time
        elapsed_time = end_time - start_time
        times.append(elapsed_time)

        print(f"Round {round_num}: {elapsed_time:,} ns")

    # Calculate average time
    avg_time = sum(times) / len(times)
    print(f"\nAverage Time (Non-Multithreading): {avg_time:,.0f} ns")
    print(f"Average Time: {avg_time / 1000000:.2f} ms")

    return times


if __name__ == "__main__":
    non_multithreading_test()