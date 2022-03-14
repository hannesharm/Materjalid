from datetime import datetime

today = datetime(2022, 3, 14)
other_date = datetime(2021, 8, 13)

delta = today - other_date

print(delta.total_seconds())
