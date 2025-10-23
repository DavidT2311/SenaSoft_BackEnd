from datetime import date


def format_date_time(date: date):
    return date.replace(tzinfo=None) if date.tzinf else date
