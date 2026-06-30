MAX_WEIGHT = 20

print("Enter maximum number of items to be shipped:")
max_items = int(input())

current_weight = 0
packages_sent = 0
total_weight = 0

current_package_number = 1

package_unused = []  # stores (package_number, unused_capacity)

items_count = 0

while items_count < max_items:
    try:
        print("\nEnter item weight (1-10 kg, or 0 to stop):")
        weight = int(input())

        # Stop condition
        if weight == 0:
            break

        # Validate range
        if weight < 1 or weight > 10:
            print("Invalid weight! Must be between 1 and 10.")
            continue

        # If item doesn't fit → send package
        if current_weight + weight > MAX_WEIGHT:
            packages_sent += 1
            total_weight += current_weight

            unused = MAX_WEIGHT - current_weight
            package_unused.append((current_package_number, unused))

            print(f"Package {current_package_number} sent ({current_weight} kg)")

            current_package_number += 1
            current_weight = weight
        else:
            current_weight += weight

        items_count += 1

    except ValueError:
        print("Invalid input! Please enter a number.")

# send last package if not empty
if current_weight > 0:
    packages_sent += 1
    total_weight += current_weight
    unused = MAX_WEIGHT - current_weight
    package_unused.append((current_package_number, unused))

# total unused capacity
total_unused = packages_sent * MAX_WEIGHT - total_weight

# find worst package (max unused space)
worst_package = max(package_unused, key=lambda x: x[1], default=(0, 0))

# RESULTS
print("\n========== RESULTS ==========")
print("Number of packages sent:", packages_sent)
print("Total weight:", total_weight)
print("Total unused capacity:", total_unused)

print("\nPackage with most unused capacity:")
print("Package number:", worst_package[0])
print("Unused capacity:", worst_package[1])
print("=============================")