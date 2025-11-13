class HashTable:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)

        # If bucket is empty, create first node
        if self.table[index] is None:
            self.table[index] = self.Node(key, value)
            self.size += 1
        else:
            # If bucket has nodes, traverse to check for existing key or add new
            current = self.table[index]
            prev = None

            while current:
                if current.key == key:  # Update existing key
                    current.value = value
                    return
                prev = current
                current = current.next

            # Add new node at end of chain
            prev.next = self.Node(key, value)
            self.size += 1

    def search(self, key):
        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return True
            prev = current
            current = current.next
        return False

    def print_table(self):
        print("\n--- Hash Table Structure ---")
        for i in range(self.capacity):
            print(f"Bucket {i}: ", end="")
            current = self.table[i]
            if current is None:
                print("Empty")
            else:
                while current:
                    print(f"[{current.key}: {current.value.name}] -> ", end="")
                    current = current.next
                print("END")

    def display_inventory(self):
        print("\n--- HX BABY STORE - Current Products ---")
        count = 0
        for i in range(self.capacity):
            current = self.table[i]
            while current:
                product = current.value
                print(f"{count + 1}. {product}")
                count += 1
                current = current.next
        if count == 0:
            print("No products in inventory.")


class BabyProduct:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"ID: {self.product_id} | {self.name} | RM{self.price:.2f} | Qty: {self.quantity}"


def main():
    print("=" * 50)
    print("       HX BABY STORE INVENTORY SYSTEM")
    print("=" * 50)

    # Create hash table
    inventory = HashTable(capacity=8)

    # Pre-defined products for HX BABY STORE
    sample_products = [
        BabyProduct("HX001", "Mamy Pokko Baby Diapers", 29.90, 45),
        BabyProduct("HX002", "Baby Wipes", 12.80, 85),
        BabyProduct("HX003", "Goat Baby Shampoo", 19.50, 35),
        BabyProduct("HX004", "Anti-Colic Baby Bottle", 15.75, 60),
        BabyProduct("HX005", "Baby Body Lotion", 17.25, 40),
        BabyProduct("HX006", "Baby Thermometer", 42.00, 20),
        BabyProduct("HX007", "Baby Nasal Aspirator", 8.90, 55),
        BabyProduct("HX008", "Baby Nail Clipper Set", 6.50, 75)
    ]

    # Insert sample products into hash table
    for product in sample_products:
        inventory.insert(product.product_id, product)

    # Main menu loop
    while True:
        print("\n" + "-" * 40)
        print("        HX BABY STORE MENU")
        print("-" * 40)
        print("1. View All Products")
        print("2. View Hash Table Structure")
        print("3. Search Product")
        print("4. Add New Product")
        print("5. Delete Product")
        print("6. Exit to Performance Test")
        print("-" * 40)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            inventory.display_inventory()

        elif choice == "2":
            inventory.print_table()
            print(f"\nHash Table Stats: {inventory.size} items, {inventory.capacity} buckets")

        elif choice == "3":
            product_id = input("Enter Product ID (e.g., HX001): ").strip().upper()
            product = inventory.search(product_id)
            if product:
                print(f"\n✅ PRODUCT FOUND: {product}")
            else:
                print(f"\n❌ Product '{product_id}' not found!")

        elif choice == "4":
            print("\n➕ ADD NEW PRODUCT")
            product_id = input("Product ID (HX format): ").strip().upper()
            name = input("Product Name: ").strip()
            try:
                price = float(input("Price: RM"))
                quantity = int(input("Quantity: "))

                # Check if product ID already exists
                if inventory.search(product_id):
                    print(f"❌ Product ID '{product_id}' already exists!")
                else:
                    new_product = BabyProduct(product_id, name, price, quantity)
                    inventory.insert(product_id, new_product)
                    print(f"✅ New product '{name}' added successfully!")
            except ValueError:
                print("❌ Invalid input! Please enter valid numbers.")

        elif choice == "5":
            product_id = input("Enter Product ID to delete: ").strip().upper()
            if inventory.delete(product_id):
                print(f"✅ Product '{product_id}' deleted successfully!")
            else:
                print(f"❌ Product '{product_id}' not found!")

        elif choice == "6":
            print("\nExiting to Performance Comparison...")
            break

        else:
            print("❌ Invalid choice! Please enter 1-6.")


if __name__ == "__main__":
    main()