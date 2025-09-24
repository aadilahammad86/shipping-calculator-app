def calculate_shipping_cost(weight, distance, rate):
    """
    Calculates the shipping cost based on weight, distance, and a rate.

    Args:
        weight (float): The weight of the package in kilograms.
        distance (float): The distance for the shipping in kilometers.
        rate (float): The cost per kilogram per kilometer.

    Returns:
        float: The total calculated shipping cost.
    """
    if weight <= 0 or distance <= 0 or rate <= 0:
        return 0  # Invalid input

    shipping_cost = weight * distance * rate
    return shipping_cost

# Example Usage
if __name__ == "__main__":
    pkg_weight = 10  # kg
    shipping_distance = 500  # km
    cost_rate = 0.05  # $ per kg per km

    total_cost = calculate_shipping_cost(pkg_weight, shipping_distance, cost_rate)

    print(f"Package Weight: {pkg_weight} kg")
    print(f"Shipping Distance: {shipping_distance} km")
    print(f"Rate: ${cost_rate}/kg-km")
    print("-" * 20)
    print(f"Total Shipping Cost: ${total_cost:.2f}")
