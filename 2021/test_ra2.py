from contextlib import redirect_stdout
from io import StringIO
from time import perf_counter_ns
from unittest import TestCase
from unittest.mock import MagicMock, patch
import os
from ra2 import *


class Tester(TestCase):
    def test(self):
        n = os.path.basename(__file__).replace('.py', '').replace('test_', '')
        p = os.path.join(os.path.dirname(__file__), 'data/')
        ipath = sorted(p + f for f in os.listdir(p) if n in f and 'inp' in f)
        opath = sorted(p + f for f in os.listdir(p) if n in f and 'out' in f)
        for ts_no in range(len(ipath)):
            with open(ipath[ts_no], 'r') as f:
                inputs = [line.strip('\n') for line in f.readlines()]
            with open(opath[ts_no], 'r') as f:
                outputs = [line.strip('\n') for line in f.readlines()]
            m = MagicMock()
            f = StringIO()
            length = len(inputs)
            start = perf_counter_ns()
            with redirect_stdout(f):
                with patch('builtins.input', side_effect=inputs):
                    reader()
                    for _ in range(length):
                        m()
            result = f.getvalue().split('\n')[:-1]
            for case_no, (actual, expected) in enumerate(zip(result, outputs)):
                self.assertEqual(actual, expected)
            end = perf_counter_ns()
            print(f'Test Set {ts_no + 1}: {len(outputs)} tests passed '
                  f'in {(end - start) // int(1e6):,}ms')


if __name__ == '__main__':
    tester = Tester()
    tester.test()
