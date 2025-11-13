import time
from q1_hash import HashTable, BabyProduct


def simple_performance_test():
    print("=" * 50)
    print("PERFORMANCE COMPARISON: Hash Table vs Array")
    print("=" * 50)

    # 1. Insert same data into both structures
    products_data = [
        ("HX001", "Mamy Pokko Baby Diapers", 29.90, 45),
        ("HX002", "Baby Wipes", 12.80, 85),
        ("HX003", "Goat Baby Shampoo", 19.50, 35),
        ("HX004", "Anti-Colic Baby Bottle", 15.75, 60),
        ("HX005", "Baby Body Lotion", 17.25, 40)
    ]

    # Create both data structures
    hash_table = HashTable()
    array_products = []

    # Insert same data into both
    for product_id, name, price, quantity in products_data:
        product = BabyProduct(product_id, name, price, quantity)
        hash_table.insert(product_id, product)
        array_products.append(product)

    print("Same data inserted into both Hash Table and Array")
    print(f"Products: {len(array_products)}")

    # 2. Measure execution time for searching
    search_id = "HX003"  # Product to search for
    iterations = 10000  # Number of searches

    print(f"\nSearching for: {search_id}")
    print(f"Number of searches: {iterations}")

    # Hash Table search time
    start_time = time.perf_counter_ns()
    for _ in range(iterations):
        hash_table.search(search_id)
    hash_time = (time.perf_counter_ns() - start_time) / iterations / 1000

    # Array search time
    start_time = time.perf_counter_ns()
    for _ in range(iterations):
        for product in array_products:
            if product.product_id == search_id:
                break
    array_time = (time.perf_counter_ns() - start_time) / iterations / 1000

    # 3. Display results
    print(f"\nRESULTS:")
    print(f"Hash Table: {hash_time:.3f} microseconds per search")
    print(f"Array:      {array_time:.3f} microseconds per search")

    # 4. Analysis
    print(f"\nANALYSIS:")
    if hash_time < array_time:
        speedup = ((array_time - hash_time) / array_time) * 100
        print(f"• Hash Table is {speedup:.1f}% faster")
        print(f"• Reason: Hash Table uses O(1) direct access via hash function")
        print(f"• Array uses O(n) linear search, checking each element")
    else:
        print("• Similar performance due to small dataset size")
        print("• Hash table overhead vs array simplicity")

    # 5. Conclusion
    print(f"\nCONCLUSION:")
    print("Hash tables are superior for search operations because:")
    print("• O(1) average case vs O(n) worst case for arrays")
    print("• Performance advantage grows with larger datasets")
    print("• Ideal for inventory systems with frequent searches")


if __name__ == "__main__":
    simple_performance_test()