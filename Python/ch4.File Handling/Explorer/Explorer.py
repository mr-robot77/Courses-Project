import os


def explore(ttype, address):
    result = {}
    for root, dirs, files in os.walk(address):
        for file in files:
            if file.lower().endswith("." + ttype.lower()):
                path = os.path.join(root, file)
                relative_path = os.path.relpath(path)
                directory = relative_path[:relative_path.rfind("/")]
                if directory not in result:
                    result[directory] = 1
                else:
                    result[directory] += 1
    return result