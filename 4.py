def calculate_percentage(revenue, total_revenue):
    if total_revenue == 0:
        return 0
    return (revenue / total_revenue) * 100


def display_percentages(revenue_by_state):
    total_revenue = sum(revenue_by_state.values())
    if total_revenue == 0:
        return

    for state, revenue in revenue_by_state.items():
        percentage = calculate_percentage(revenue, total_revenue)
        print(f"{state}: {percentage:.2f}%")


if __name__ == "__main__":
    revenue_by_state = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Others": 19849.53,
    }

    display_percentages(revenue_by_state)
