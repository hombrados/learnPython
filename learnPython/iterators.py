class Every_five():
    
    def __init__(self, number=20):
        self.number = number

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.number:
            returned_value = self.value
            self.value += 5
            return returned_value
        else:
            raise StopIteration


if __name__=='__main__':
    numbers = Every_five(40)
    for i in numbers:
        print(i)

