
import pytest

def test_key():
    key = ('0000000000true')
    keyno = key[0:10]
    result = str('t' in keyno or 'r' in keyno or 'u' in keyno or 'e' in keyno)
    assert result == 'False'

