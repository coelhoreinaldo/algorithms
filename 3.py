import json


def read_revenue_from_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return [day["valor"] for day in data if "valor" in day]


def calculate_min_max_average(revenue):
    total_revenue = 0
    revenue_days = 0
    min_value = float("inf")
    max_value = float("-inf")

    for value in revenue:
        if value > 0:
            total_revenue += value
            revenue_days += 1
            if value < min_value:
                min_value = value
            if value > max_value:
                max_value = value

    average = total_revenue / revenue_days if revenue_days > 0 else 0
    return min_value, max_value, average


def count_days_above_average(revenue, average):
    days_above_average = 0
    for value in revenue:
        if value > 0 and value > average:
            days_above_average += 1
    return days_above_average


if __name__ == "__main__":
    file_path = "3-data.json"
    daily_revenue = read_revenue_from_file(file_path)

    min_value, max_value, average_revenue = calculate_min_max_average(daily_revenue)

    days_above_avg = count_days_above_average(daily_revenue, average_revenue)

    print(f"Minimum revenue: ${min_value:.2f}")
    print(f"Maximum revenue: ${max_value:.2f}")
    print(f"Average revenue: ${average_revenue:.2f}")
    print(f"Days with revenue above average: {days_above_avg}")
