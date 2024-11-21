from icalendar import Calendar, Event
from datetime import datetime, timedelta
import pytz

# Define a function to create events
def create_event(start_time, end_time, summary, day_offset):
    event = Event()
    event.add('summary', summary)
    event.add('dtstart', start_time + timedelta(days=day_offset))
    event.add('dtend', end_time + timedelta(days=day_offset))
    event.add('dtstamp', datetime.now(pytz.utc))
    return event

# Initialize the calendar
cal = Calendar()

# Define timezone
timezone = pytz.timezone('Australia/Sydney')

# Weekly schedule
schedule = {
    'Monday': [
        ("7:00", "7:10", "Wake up"),
        ("7:10", "7:20", "Journal writing"),
        ("7:30", "8:00", "Breakfast"),
        ("8:00", "9:00", "AWS course"),
        ("9:00", "9:15", "Clean room"),
        ("9:15", "10:15", "Study LeetCode"),
        ("10:15", "10:45", "Study English"),
        ("11:00", "14:00", "Socializing"),
        ("14:00", "14:30", "Lunch"),
        ("14:30", "15:00", "Rest"),
        ("15:00", "18:00", "Free time for spontaneous tasks"),
        ("18:00", "19:00", "Dinner"),
        ("19:00", "19:10", "Journal writing"),
        ("20:00", "21:00", "Wind down"),
        ("22:00", "22:30", "Prepare for sleep"),
        ("23:00", "23:59", "Sleep")
    ],
    'Tuesday': [
        ("7:00", "7:10", "Wake up"),
        ("7:10", "7:25", "Ba Duan Jin"),
        ("7:30", "8:00", "Breakfast"),
        ("8:00", "9:00", "AWS course"),
        ("9:00", "9:15", "Clean room"),
        ("9:15", "10:15", "Study LeetCode"),
        ("10:15", "11:15", "Strength training"),
        ("11:15", "11:45", "Study English"),
        ("12:00", "15:00", "Prepare meal prep"),
        ("15:00", "15:30", "Lunch"),
        ("15:30", "16:00", "Rest"),
        ("16:00", "18:00", "Take cat to vet"),
        ("18:00", "19:00", "Dinner"),
        ("19:00", "19:10", "Journal writing"),
        ("20:00", "21:00", "Wind down"),
        ("22:00", "22:30", "Prepare for sleep"),
        ("23:00", "23:59", "Sleep")
    ],
    'Wednesday': [
        ("7:00", "7:10", "Wake up"),
        ("7:10", "7:25", "Ba Duan Jin"),
        ("7:30", "8:00", "Breakfast"),
        ("8:00", "9:00", "AWS course"),
        ("9:00", "9:15", "Clean room"),
        ("9:15", "10:15", "Study LeetCode"),
        ("10:15", "10:45", "Study English"),
        ("11:00", "15:00", "Job search"),
        ("15:00", "15:30", "Lunch"),
        ("15:30", "16:00", "Rest"),
        ("16:00", "18:00", "Free time for spontaneous tasks"),
        ("18:00", "19:00", "Dinner"),
        ("19:00", "19:10", "Journal writing"),
        ("20:00", "21:00", "Wind down"),
        ("22:00", "22:30", "Prepare for sleep"),
        ("23:00", "23:59", "Sleep")
    ],
    'Thursday': [
        ("7:00", "7:10", "Wake up"),
        ("7:10", "7:20", "Journal writing"),
        ("7:30", "8:00", "Breakfast"),
        ("8:00", "9:00", "AWS course"),
        ("9:00", "9:15", "Clean room"),
        ("9:15", "10:15", "Study LeetCode"),
        ("10:15", "10:45", "Study English"),
        ("11:00", "14:00", "Prepare meal prep"),
        ("14:00", "14:30", "Lunch"),
        ("14:30", "15:00", "Rest"),
        ("15:00", "18:00", "Free time for spontaneous tasks"),
        ("18:00", "19:00", "Dinner"),
        ("19:00", "19:10", "Journal writing"),
        ("20:00", "21:00", "Wind down"),
        ("22:00", "22:30", "Prepare for sleep"),
        ("23:00", "23:59", "Sleep")
    ],
    'Friday': [
        ("7:00", "7:10", "Wake up"),
        ("7:10", "7:25", "Ba Duan Jin"),
        ("7:30", "8:00", "Breakfast"),
        ("8:00", "9:00", "AWS course"),
        ("9:00", "9:15", "Clean room"),
        ("9:15", "10:15", "Study LeetCode"),
        ("10:15", "11:15", "Strength training"),
        ("11:15", "11:45", "Study English"),
        ("12:00", "15:00", "Grocery shopping"),
        ("15:00", "15:30", "Lunch"),
        ("15:30", "16:00", "Rest"),
        ("16:00", "18:00", "Free time for spontaneous tasks"),
        ("18:00", "19:00", "Dinner"),
        ("19:00", "19:10", "Journal writing"),
        ("20:00", "21:00", "Wind down"),
        ("22:00", "22:30", "Prepare for sleep"),
        ("23:00", "23:59", "Sleep"),
    ],
    'Saturday': [
        ("7:00", "7:10", "Wake up"),
        ("7:10", "7:25", "Ba Duan Jin"),
        ("7:30", "8:00", "Breakfast"),
        ("8:00", "9:00", "Run"),
        ("9:00", "9:15", "Clean room"),
        ("9:15", "12:00", "Free time for spontaneous tasks"),
        ("12:00", "12:30", "Lunch"),
        ("12:30", "13:00", "Rest"),
        ("13:00", "15:00", "Weekend review"),
        ("15:00", "16:00", "Xiaohongshu post"),
        ("16:00", "18:00", "Free time for spontaneous tasks"),
        ("18:00", "19:00", "Dinner"),
        ("19:00", "19:10", "Journal writing"),
        ("20:00", "21:00", "Wind down"),
        ("22:00", "22:30", "Prepare for sleep"),
        ("23:00", "23:59", "Sleep"),
    ],
    'Sunday': [
        ("7:00", "7:10", "Wake up"),
        ("7:10", "7:20", "Journal writing"),
        ("7:30", "8:00", "Breakfast"),
        ("8:00", "9:00", "AWS course"),
        ("9:00", "9:15", "Clean room"),
        ("9:15", "10:15", "Study LeetCode"),
        ("10:15", "10:45", "Study English"),
        ("11:00", "14:00", "Free time for spontaneous tasks"),
        ("14:00", "14:30", "Lunch"),
        ("14:30", "15:00", "Rest"),
        ("15:00", "18:00", "Half-day complete rest"),
        ("18:00", "19:00", "Dinner"),
        ("19:00", "19:10", "Journal writing"),
        ("20:00", "21:00", "Wind down"),
        ("22:00", "22:30", "Prepare for sleep"),
        ("23:00", "23:59", "Sleep"),
    ]
}

# Create events for each day
start_date = datetime(2024, 11, 18, 0, 0, tzinfo=timezone)
day_index = 0
for day, tasks in schedule.items():
    for task in tasks:
        start_time = datetime.strptime(task[0], "%H:%M").replace(year=start_date.year, month=start_date.month, day=start_date.day, tzinfo=timezone)
        end_time = datetime.strptime(task[1], "%H:%M").replace(year=start_date.year, month=start_date.month, day=start_date.day, tzinfo=timezone)
        cal.add_component(create_event(start_time, end_time, task[2], day_index))
    day_index += 1

# Save to .ics file
with open('weekly_detailed_schedule.ics', 'wb') as f:
    f.write(cal.to_ical())

print("iCalendar file created: weekly_detailed_schedule.ics")