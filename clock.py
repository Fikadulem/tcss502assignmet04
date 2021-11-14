from datetime import datetime


class Clock:
    # Instantiate the clock class
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def hour(self):
        return self.__hour

    def minute(self):
        return self.__minute

    def second(self):
        return self.__second

    # method to set hour
    def set_hour(self, new_hour):
        if isinstance(new_hour, int):
            the_hour = new_hour
            if 0 <= the_hour <= 23:
                self.__hour = the_hour
            else:
                raise ValueError("Value should be between 00 and 23")

    # method set minute
    def set_minute(self, new_minute):
        if isinstance(new_minute, int):
            the_minute = int(new_minute)
            if 0 <= the_minute <= 59:
                self.__minute = the_minute
            else:
                raise ValueError("Value should be between 00 and 59")

    # method to set second
    def set_second(self, new_second):
        if isinstance(new_second, int):
            the_second = int(new_second)
            if 0 <= the_second <= 59:
                self.__second = the_second
            else:
                raise ValueError("Value should be between 00 and 59")

    # method to advance hour
    def advance_hour(self, amount_to_advance):
        if isinstance(amount_to_advance, int):
            amount_to_advance = int(amount_to_advance)
            if 00 <= amount_to_advance:
                amount_to_advance = amount_to_advance
            else:
                raise ValueError("Value should be between 00 and 59")
        time_tot = self.__hour + amount_to_advance
        hour = time_tot % 24
        self.__hour = hour

    # method to advance minute

    def advance_minute(self, amount_to_advance):
        if isinstance(amount_to_advance, int):
            amount_to_advance = int(amount_to_advance)
            if 0 <= amount_to_advance:
                amount_to_advance = amount_to_advance
            else:
                raise ValueError("Value should be between 00 and 59")
        time_tot = (self.__hour * 60) + self.__minute + amount_to_advance
        hour = time_tot // 60
        minute = time_tot % 60
        self.__hour = hour
        self.__minute = minute

    # method to set minute to new minute
    def set_to_current_time(self):
        now = datetime.now()
        self.__hour = now.hour
        self.__minute = now.hour
        self.__second = now.second

    # method to format time to string
    def __str__(self):
        return f'{self.__hour}:{self.__minute}:{self.__second}'

    # method to repr
    def __repr__(self):
        return f'{self.__hour}:{self.__minute}:{self.__second}'

    # method to compare if time is equal
    def __eq__(self, other):
        if isinstance(other, Clock):
            return self.__hour == other.hour() and self.__minute == other.minute() and self.__second == other.second()
        return False

    # method to compare if time is lessthan
    def __lt__(self, other):
        if isinstance(other, Clock):
            if self.__hour < other.__hour:
                return True
            elif self.__hour == other.__hour and self.__minute < other.__minute:
                return True
            elif self.__hour == other.__hour and self.__minute == other.__minute and self.__second < other.__second:
                return True
            else:
                return False
        raise Exception("other argument to less than was not a Clock: " % other)

    # method to compare if time is greater than
    def __gt__(self, other):
        if isinstance(other, Clock):
            if self.__hour > other.__hour:
                return True
            elif self.__hour == other.__hour and self.__minute > other.__minute:
                return True
            elif self.__hour == other.__hour and self.__minute == other.__minute and self.__second > other.__second:
                return True
            else:
                return False
        raise Exception("other argument to less than was not a Clock: " % other)
