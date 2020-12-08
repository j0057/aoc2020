class LoopVM:
    def __init__(self):
        self.ip = 0
        self.acc = 0

    @classmethod
    def parse(cls, lines):
        vm = cls()
        vm.code = [vm.parse_instruction(line) for line in lines]
        return vm

    def parse_instruction(self, line):
        opcode, *args = line.split()
        return (getattr(self, f"_op_{opcode}"), tuple(int(a) for a in args))

    def _op_nop(self, _):
        return +1

    def _op_jmp(self, p1):
        return p1

    def _op_acc(self, p1):
        self.acc += p1
        return +1

    def trace_loop(self):
        trace = set()
        while self.ip < len(self.code):
            op, args = self.code[self.ip]
            if self.ip in trace:
                break
            else:
                trace |= {self.ip}
            self.ip += op(*args)

def day08a(lines):
    vm = LoopVM.parse(lines)
    vm.trace_loop()
    return vm.acc

ex1 = 'nop +0|acc +1|jmp +4|acc +3|jmp -3|acc -99|acc +1|jmp -4|acc +6'.split('|')

def test_08_ex1(): assert day08a(ex1) == 5

def test_08a(day08_lines): assert day08a(day08_lines) == 1782
