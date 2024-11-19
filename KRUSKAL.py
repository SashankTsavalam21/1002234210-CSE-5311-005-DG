
class Activity:
    def __init__(self, name, start_time, end_time):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

def compare_by_end_time(activity1, activity2):
    return activity2.end_time - activity1.end_time

schedule = [
    Activity("reading", 7, 9),
    Activity("exercise", 5, 6),
    Activity("meal", 12, 13),
    Activity("work", 9, 17),
    Activity("meditation", 6, 7),
    Activity("study", 8, 10),
    Activity("breakfast", 6, 7),
    Activity("nap", 15, 16),
    Activity("dinner", 18, 19)
]

schedule.sort(key=lambda activity: activity.end_time, reverse=True)

print("Sorted Daily Schedule:")
for activity in schedule:
    print(activity.name)
