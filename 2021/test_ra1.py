from time import perf_counter_ns
from unittest import TestCase
from ra1 import *
import os


class Tester(TestCase):
    def set_up(self):
        n = os.path.basename(__file__).replace('.py', '').replace('test_', '')
        p = os.path.join(os.path.dirname(__file__), 'data\\').replace('\\', '/')
        i = [p + f for f in os.listdir('data') if n in f and 'inp' in f]
        o = [p + f for f in os.listdir('data') if n in f and 'out' in f]
        data = []
        for ts_no in range(len(i)):
            with open(i[ts_no], 'r') as f:
                ti = f.readlines()
            with open(o[ts_no], 'r') as f:
                to = f.readlines()
            tmp = {i + 1: {'N': int(ti[i * 2].strip('\n').split()[0]),
                           'K': int(ti[i * 2].strip('\n').split()[1]),
                           'S': ti[i * 2 + 1].strip('\n'),
                           'expected': to[i].strip('\n')}
                   for i in range(int(ti.pop(0)))}
            data.append(tmp)
        self.data = data

    def test_func(self, opt='silent'):
        self.set_up()
        for no, test_set in enumerate(self.data):
            start = perf_counter_ns()
            for i in range(len(test_set)):
                t = test_set[i + 1]
                n, k, s = t['N'], t['K'], t['S']
                e = int(t['expected'][t['expected'].index(':') + 2:])
                actual = num_ops(n, k, s)
                self.assertEqual(e, actual)
                if opt == 'verbose':
                    print(f'Test Set {no + 1}: Test {i + 1} Passed')
            end = perf_counter_ns()
            print(f'Test Set {no + 1}: {len(test_set)} tests passed '
                  f'in {end - start:,}ns')


if __name__ == '__main__':
    tester = Tester()
    tester.test_func()
