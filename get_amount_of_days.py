import calendar

def days_per_month(year):
    return {calendar.month_name[m]: calendar.monthrange(year, m)[1] for m in range(1, 13)}

# Example
for y in [2025, 2026, 2027]:
    print(f"{y}: {days_per_month(y)}")

