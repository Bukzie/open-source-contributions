class Node:
    def __del__(self):
        self.closed = 1 + 1  # anything mutmut can mutate, so __del__ gets a trampoline


def make_garbage(n):
    a, b = Node(), Node()
    a.other, b.other = b, a  # reference cycle: freed only by the cyclic GC
    a.junk = [[] for _ in range(n)]  # vary allocations so GC fires at varying points
    return 1 + 1
