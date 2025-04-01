from datetime import datetime
import pytz

timezone = pytz.timezone("Europe/Moscow")

class Today:
    def date():
        return datetime.now().strftime("%d")

    def month(option="number"):
        format_option = "%m"
        if option == "word":
            format_option = "%M"
        return datetime.now().strftime(format_option)

    def year():
        pass

    def seconds():
        pass

    def minutes():
        pass

    def hours():
        pass

    def weekday():
        pass

print(Today.month("word"))

