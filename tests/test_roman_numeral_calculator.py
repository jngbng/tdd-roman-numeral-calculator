import pytest
from roman_numeral_calculator import add

def test_adding_Is():
    assert add('I', 'I') == 'II'
    assert add('I', 'II') == 'III'


bad_inputs = [2, None, 'Z', 'L', 'C', 'D', 'M']

@pytest.mark.parametrize('bad_input', bad_inputs)
def test_augend_out_of_scope_raise_exceptions(bad_input):
    with pytest.raises(ValueError):
        add('I', bad_input)


@pytest.mark.parametrize('bad_input', bad_inputs)
def test_addend_out_of_scope_raise_exceptions(bad_input):
    with pytest.raises(ValueError):
        add(bad_input, 'I')


def test_IV_and_V():
    assert add('II', 'II') == 'IV'
    assert add('III', 'II') == 'V'
    assert add('IV', 'I') == 'V'
    assert add('V', 'I') == 'VI'
    assert add('I', 'V') == 'VI'


def test_IX_and_X():
    assert add('V', 'V') == 'X'
    assert add('V', 'IV') == 'IX'
    assert add('VIII', 'I') == 'IX'
    assert add('IX', 'I') == 'X'
    assert add('X', 'I') == 'XI'
    assert add('I', 'X') == 'XI'
    assert add('X', 'V') == 'XV'
    assert add('V', 'X') == 'XV'
    assert add('X', 'X') == 'XX'
