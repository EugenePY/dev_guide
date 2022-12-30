import re


def parse(input_string):
    prog = re.compile(r'\d+')  # <interger>
    a = prog.findall(input_string)
    return int(a[0])

class Key:
    def __init__(self, a) -> None:
        self.a = a

def parse_kle(src):
    ...
