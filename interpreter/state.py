from .getch import getch


class State:
    def __init__(self):
        self.tape = [0]
        self.index = 0
        self.neg_offset = 0

    def r(self):
        self.index += 1

        if self.neg_offset + len(self.tape) - 1 < self.index:
            self.tape.append(0)

    def l(self):
        self.index -= 1

        if self.neg_offset > self.index:
            self.neg_offset -= 1

            self.tape.insert(0, 0)

    def inc(self):
        self.tape[self.index - self.neg_offset] += 1

    def dec(self):
        self.tape[self.index - self.neg_offset] -= 1

    def print(self):
        print(chr(self.tape[self.index - self.neg_offset]), end="", flush=True)

    def read(self):
        self.tape[self.index - self.neg_offset] = ord(getch())

    def is_zero(self):
        return self.tape[self.index - self.neg_offset] == 0