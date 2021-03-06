class PrepareTxtFileToDatabase:
    def __init__(self, path):
        self.path = path

    def prepare(self, callback=()):
        with open(self.path, mode="r", encoding="ISO-8859-1") as file:
            for item in file:
                list_of_line = item.split(sep="<SEP>")
                callback(list_of_line)