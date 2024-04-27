# find number of days present in two dates
from datetime import datetime
def days_between_dates(date1, date2):
  date_format = "%Y-%m-%d"
  date1_obj = datetime.strptime(date1, date_format)
  date2_obj = datetime.strptime(date2, date_format)
  delta = abs(date2_obj - date1_obj)
  return delta.days
date1 = "2024-04-01"
date2 = "2024-04-10"
print("Number of days between", date1, "and", date2, ":", days_between_dates(date1, date2))