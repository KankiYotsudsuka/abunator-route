
import pytest
import psycopg2
import last  # テスト対象のモジュールをインポートする


def test_key():
    keyno = last.keyMaker('0000000000true')
    result = str('t' in keyno or 'r' in keyno or 'u' in keyno or 'e' in keyno)
    assert result == 'False'

