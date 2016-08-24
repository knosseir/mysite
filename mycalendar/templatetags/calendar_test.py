from django import template
import datetime
from datetime import timedelta


register = template.Library()

@register.simple_tag
def getMonth():
    d = datetime.date.today()

    return {1:'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December',
    }[d.month]

@register.simple_tag
def getMonthStartDOW():
    d = datetime.date.today()
    dow = datetime.date(d.year, d.month, 1) #1st day of the month
    return dow.weekday()

def getWeekSunday():
    d = datetime.date.today()
    sunday = d - timedelta(days=d.isoweekday())
    return sunday

def getWeekSaturday():
    d = datetime.date.today()
    sunday = d - timedelta(days=d.isoweekday())
    saturday = sunday + timedelta(days=6)
    return saturday

@register.simple_tag
def getWeekdayInterval():
    weekdays = getMonth() + " " + str(getWeekSunday().day) + " - " + str(getWeekSaturday().day) + ", " + str(datetime.date.today().year)
    return weekdays