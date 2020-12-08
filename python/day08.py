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

    def reset(self):
        self.__init__()
        self.code = self.code_[:]

    def hack_jmp_nop(self):
        self.code_ = self.code[:]
        for (i, (op, args)) in enumerate(self.code_):
            self.reset()
            if op == self._op_nop:
                self.code[i] = (self._op_jmp, args)
            elif op == self._op_jmp:
                self.code[i] = (self._op_nop, args)
            self.trace_loop()
            if self.ip == len(self.code):
                break

def day08a(lines):
    vm = LoopVM.parse(lines)
    vm.trace_loop()
    return vm.acc

def day08b(lines):
    vm = LoopVM.parse(lines)
    vm.hack_jmp_nop()
    return vm.acc

ex1 = 'nop +0|acc +1|jmp +4|acc +3|jmp -3|acc -99|acc +1|jmp -4|acc +6'.split('|')

def test_08_ex1(): assert day08a(ex1) == 5
def test_08_ex2(): assert day08b(ex1) == 8

def test_08a(day08_lines): assert day08a(day08_lines) == 1782
def test_08b(day08_lines): assert day08b(day08_lines) == 797
