
class ConverterInterface:
    def convert(self, source, dest, amount):
        pass

class ConverterImpl(ConverterInterface):
    def convert(self, source, dest, amount):
        return amount * self.get_rate(source, dest)

    def get_rate(self, source, dest):
        return 0.5

