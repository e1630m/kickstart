from contextlib import redirect_stdout
from time import perf_counter_ns
from unittest import TestCase
from unittest.mock import MagicMock, patch
import io
import os
from ra1 import *


class Tester(TestCase):
    def test(self, opt='silent'):
        n = os.path.basename(__file__).replace('.py', '').replace('test_', '')
        p = os.path.join(os.path.dirname(__file__), 'data\\').replace('\\', '/')
        i = [p + f for f in os.listdir('data') if n in f and 'inp' in f]
        o = [p + f for f in os.listdir('data') if n in f and 'out' in f]
        for ts_no in range(len(i)):
            with open(i[ts_no], 'r') as f:
                ti = [line.strip('\n') for line in f.readlines()]
            with open(o[ts_no], 'r') as f:
                to = [line.strip('\n') for line in f.readlines()]
            m = MagicMock()
            f = io.StringIO()
            m.side_effect = ti
            length = len(ti)
            with redirect_stdout(f):
                with patch('builtins.input', side_effect=ti):
                    reader()
                    start = perf_counter_ns()
                    for _ in range(length):
                        m()
            end = perf_counter_ns()
            result = f.getvalue().split('\n')[:-1]
            if opt == 'verbose':
                for case, (actual, expected) in enumerate(zip(result, to)):
                    self.assertEqual(actual, expected)
                    print(f'Test Set {ts_no + 1}: Test {case + 1} Passed')
            print(f'Test Set {ts_no + 1}: {len(to)} tests passed '
                  f'in {end - start:,}ns')


if __name__ == '__main__':
    tester = Tester()
    tester.test()
