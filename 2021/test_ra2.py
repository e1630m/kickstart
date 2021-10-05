from time import perf_counter_ns
from unittest import TestCase
from ra2 import *
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
            num_tests = int(ti.pop(0))
            grids = {}
            for t_no in range(num_tests):
                r, c = map(int, ti.pop(0).strip('\n').split())
                tmp = []
                for _ in range(r):
                    row = ti.pop(0)
                    tmp.append([int(n) for n in row.split()])
                grids[t_no + 1] = {'grid': tmp, 'expected': to.pop(0).strip('\n')}
            data.append(grids)
        self.data = data

    def test_func(self, opt='silent'):
        self.set_up()
        for no, test_set in enumerate(self.data):
            start = perf_counter_ns()
            for i in range(len(test_set)):
                t = test_set[i + 1]
                grid = t['grid'],
                e = int(t['expected'][t['expected'].index(':') + 2:])
                actual = funcname(grid)
                self.assertEqual(e, actual)
                if opt == 'verbose':
                    print(f'Test Set {no + 1}: Test {i + 1} Passed')
            end = perf_counter_ns()
            print(f'Test Set {no + 1}: {len(test_set)} tests passed '
                  f'in {end - start:,}ns')


if __name__ == '__main__':
    tester = Tester()
    tester.test_func()
