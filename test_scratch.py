import pytest
from unittest.mock import patch


def get_inputs(inputs: tuple) -> tuple:
    return tuple(float(input(f'Define {input_}: ')) for input_ in inputs)


def get_roots() -> float:
    a, b = get_inputs(('a', 'b'))
    return -b / a


@pytest.mark.parametrize("a, b, x", [(1, 1, 1), (1, 1.0, 1.0), (1, '1,1', 1.0)])
def test_get_roots(a, b, x):
    with patch('test_scratch.get_inputs', (a, b)):
        assert get_roots() == x


if __name__ == '__main__':
    with patch('test_scratch.get_inputs', (1, 2)):
        print(get_roots())
llllll