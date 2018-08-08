"Module for practicing date and time operations"

from datetime import datetime
import babel.dates

INPUT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S%z'

def convert_to_datetime(*args, conversion_format):
    """Function takes iterable of date strings as input.
        Returns generator for converting string to datetime objects.
    """
    return [datetime.strptime(arg, conversion_format) for arg in args]

def lc_print(dates, locale):
    for date in dates:
        print(babel.dates.format_datetime(datetime=date, locale=locale))

def main():
    "Main function"
    print('Enter two dates in format YYYY-MM-DD hh:mi:ss' + '\u00b1' + 'hhmm: ', end='')
    data = input().strip().split()
    date_one, date_two = ' '.join(data[:2]), ' '.join(data[2:])
    dates = convert_to_datetime(date_one, date_two, conversion_format=INPUT_DATE_FORMAT)
    lc_print(dates, locale='ru_RU')

if __name__ == '__main__':
    main()
