from .state import State


class Interpreter:
    def __init__(self):
        self.state = State()

        self.loop_entries = []
        self.loop_ends = {}

    def match_loops(self, prog):
        stack = []

        for i, c in enumerate(prog):
            if c == "[":
                stack.append(i)
            elif c == "]":
                if len(stack) > 0:
                    self.loop_ends[stack.pop()] = i
                else:
                    print("Error: Unmatched ']' for at command", i)

    def eval(self, prog):
        self.match_loops(prog)

        p_id = 0

        while True:
            if p_id >= len(prog):
                break

            c = prog[p_id]

            if c == ">":
                self.state.r()
            elif c == "<":
                self.state.l()
            elif c == "+":
                self.state.inc()
            elif c == "-":
                self.state.dec()
            elif c == ".":
                self.state.print()
            elif c == ",":
                self.state.read()
            elif c == "[":
                if self.state.is_zero(): # Value at current cell is zero --> jump to end of loop
                    p_id = self.loop_ends[p_id]
                else: # Go into loop
                    self.loop_entries.append(p_id)
                #print("loop enter")
            elif c == "]":
                if self.state.is_zero():
                    self.loop_entries.pop()
                    #print("loop exit")
                else:
                    p_id = self.loop_entries[-1]

            #print(len(self.loop_entries))

            p_id += 1

        if len(self.loop_entries) != 0:
            print("Error: Missing ']' for command at", self.loop_entries[-1])