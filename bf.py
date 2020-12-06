from interpreter import Interpreter


if __name__ == "__main__":
    with open("examples/rot13.bf", "r") as f:
        prog = f.read()

    interpreter = Interpreter()

    interpreter.eval(prog)
