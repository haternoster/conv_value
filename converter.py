import urllib.request
import json

class Rate_Converter:
    def convert(self, source, dest, amount):
        return amount * self.get_rate(source, dest)

    def get_rate(self, source, dest):
        source_rate = self.get_rub_rate(source)
        dest_rate = self.get_rub_rate(dest)
        return source_rate / dest_rate

    def get_rub_rate(self, source):

        if source == "RUB":
            return 1

        link = "https://www.cbr-xml-daily.ru/daily_json.js"

        contents = urllib.request.urlopen(link).read()
        parce_it = json.loads(contents)["Valute"][source.upper()]
        return parce_it["Value"] / parce_it["Nominal"]
