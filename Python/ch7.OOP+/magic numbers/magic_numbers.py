class Strint(int):
    
    def __lt__(self, other):
        return (self % 10) < (other % 10)

    def __gt__(self, other):
        return (self % 10) > (other % 10)

    def __le__(self, other):
        return (self % 10) <= (other % 10)

    def __ge__(self, other):
        return (self % 10) >= (other % 10)

    def __eq__(self, other):
        return (self % 10) == (other % 10)

    def __ne__(self, other):
        return (self % 10) != (other % 10)      

    def __add__(self, other):
        return int(str(self)+str(other))

    def __sub__(self, other):
        first = str(self)
        second = str(other)
        if first.endswith(second):
            result = first[:-(len(second))]
            if result:
                return int(result)
            return 0
        raise Exception('The subtraction is not valid!')

    def __len__(self):
        return len(str(self))

    def __call__(self):
        english_to_persian = {
            '0': '۰',
            '1': '۱',
            '2': '۲',
            '3': '۳',
            '4': '۴',
            '5': '۵',
            '6': '۶',
            '7': '۷',
            '8': '۸',
            '9': '۹'
        }
        result = ''.join([english_to_persian[decimal] for decimal in str(self)])
        return result