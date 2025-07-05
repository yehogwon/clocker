import builtins
from unittest.mock import patch

import pytest

from ticktocker.stopwatch import stopwatch


def test_stopwatch_context_manager_prints_elapsed_time():
    outputs = []
    with patch('ticktocker.stopwatch._millis', side_effect=[1000.0, 1500.0]), \
         patch('ticktocker.stopwatch.TextStyle.green', side_effect=lambda x: x), \
         patch('ticktocker.stopwatch.TextStyle.bold', side_effect=lambda x: x), \
         patch.object(builtins, 'print', lambda x: outputs.append(x)):
        with stopwatch('mydesc'):
            pass
    assert outputs == ['mydesc: 500.0000 ms']


def test_stopwatch_decorator_prints_elapsed_time():
    outputs = []
    with patch('ticktocker.stopwatch._millis', side_effect=[2000.0, 2500.0]), \
         patch('ticktocker.stopwatch.TextStyle.green', side_effect=lambda x: x), \
         patch('ticktocker.stopwatch.TextStyle.bold', side_effect=lambda x: x), \
         patch.object(builtins, 'print', lambda x: outputs.append(x)):
        @stopwatch()
        def sample():
            return 'result'

        result = sample()

    assert result == 'result'
    assert outputs == ['sample: 500.0000 ms']
