from django import template
import datetime

register = template.Library()

@register.simple_tag
def getMonth():
    d = datetime.date.today()

    if d.month == 1:
        return 'January'
    elif d.month == 2:
        return 'February'
    elif d.month == 3:
        return 'March'
    elif d.month == 4:
        return 'April'
    elif d.month == 5:
        return 'May'
    elif d.month == 6:
        return 'June'
    elif d.month == 7:
        return 'July'
    elif d.month == 8:
        return 'August'
    elif d.month == 9:
        return 'September'
    elif d.month == 10:
        return 'October'
    elif d.month == 11:
        return 'November'
    elif d.month == 12:
        return 'December'
    else:
        return "ERROR!"

@register.simple_tag
def getMonthStartDOW():
    d = datetime.date.today()
    dow = datetime.date(d.year, d.month, 1) #1st day of the month
    return dow.weekday()


@register.filter
def get_range(value):
    return range(value)

