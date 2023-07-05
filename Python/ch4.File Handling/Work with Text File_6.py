# Application of Generators in Files
def csv_reader(path):
    file = open(path)
    result = file.read().split("\n")
    return result

def csv_reader(path):
    with open(path) as file:
        for row in file:
            yield row