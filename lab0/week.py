# week.py module
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def tomorrow(day):
  tomorrow = day
  if day in week:
    n = week.index(day)
    n = n + 1
    if n == len(week):
      n = 0
      tomorrow = week[n]
  return(tomorrow)

def yesterday(day):
  yesterday = day
  if day in week:
    n = week.index(day)
    n = n - 1
    if n < 0:
      n = len(week) -1
      yesterday = week[n]
  return(yesterday)