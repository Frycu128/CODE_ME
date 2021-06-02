def academic_day(day):
    print(day.weekday())
    pl_holidays = holidays.Polish()
    if day in pl_holidays:
        return f"Today is a holiday day of {pl_holidays.get(day)}"
    else:
        if day.weekday() == 5 or day.weekday() == 6:
            return "Yeah, today is a weekend!"
        else:
            return "Nope, no leisure today."

academic_day(20)