class Helpers:

    def getStringTime(self, datetime):
        milliseconds = datetime.strftime('%f')

        return str(datetime.year) +\
            '{0:02}'.format(datetime.month) +\
            '{0:02}'.format(datetime.day) + "_" +\
            '{0:02}'.format(datetime.hour) + "h" +\
            '{0:02}'.format(datetime.minute) + "m" +\
            '{0:02}'.format(datetime.second) + "s" +\
            "-" + str(milliseconds)
