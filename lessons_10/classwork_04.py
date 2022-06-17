'''Пользователь вводит два числа N и M, рассчитать последовательность  N + NN + NNN + ... + N^M.'''


class SymbolsIterator:
    def __init__(self, symbol:str, count:int):
        self.symbol = symbol
        self.count = count
        self.current_value = symbol

    def __next__(self):
        previous_value = self.current_value
        if len(self.current_value) <= self.count:
            self.current_value += self.symbol
            return previous_value
        else:
            raise StopIteration

    def __iter__(self):
        self.current_value = self.symbol
        return self


if __name__ == "__main__":
    my_sym = SymbolsIterator(symbol="3", count=5)
    for item in my_sym:
        print(item)