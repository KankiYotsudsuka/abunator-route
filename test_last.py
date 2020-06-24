import unittest
import pytest
import psycopg2
import last  # テスト対象のモジュールをインポートする


class test_last(unittest.TestCase):
    def test_key(self):
        keyno = last.keyMaker('0000000000true')
        result = str(judge(keyno))
        self.assertEqual(result,'False')

def judge(keyno):
    return('t' in keyno or 'r' in keyno or 'u' in keyno or 'e' in keyno)

if __name__ == '__main__':
    # スクリプトとして実行された場合の処理
    unittest.main()