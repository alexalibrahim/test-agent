from unittest import TestCase

from python import (
    _str_is_bool, _str_is_int, _str_is_float, _str_is_num, _is_num,
    _escape, encode_apache, encode_erlang, encode_haproxy, encode_ini,
    encode_json, encode_logstash
)

class Test(TestCase):
    def test_encode_apache(self):
        self.fail()
    def test_str_is_bool(self):
        self.assertTrue(_str_is_bool("true"))
        self.assertTrue(_str_is_bool("false"))
        self.assertFalse(_str_is_bool("yes"))
        self.assertFalse(_str_is_bool("no"))

    def test_str_is_int(self):
        self.assertTrue(_str_is_int("123"))
        self.assertTrue(_str_is_int("-123"))
        self.assertFalse(_str_is_int("123.45"))
        self.assertFalse(_str_is_int("abc"))

    def test_str_is_float(self):
        self.assertTrue(_str_is_float("123.45"))
        self.assertTrue(_str_is_float("-123.45"))
        self.assertTrue(_str_is_float("1e10"))
        self.assertFalse(_str_is_float("abc"))

    def test_str_is_num(self):
        self.assertTrue(_str_is_num("123"))
        self.assertTrue(_str_is_num("123.45"))
        self.assertFalse(_str_is_num("abc"))

    def test_is_num(self):
        self.assertTrue(_is_num(123))
        self.assertTrue(_is_num(123.45))
        self.assertFalse(_is_num("123"))

    def test_escape(self):
        self.assertEqual(_escape("hello & world", format="xml"), "hello &amp; world")
        self.assertEqual(_escape("hello\nworld", format="control"), "hello\\nworld")
        self.assertEqual(_escape('hello "world"', quote='"'), 'hello \\"world\\"')

    def test_encode_apache(self):
        data = {"content": [{"options": {"key": "value"}}]}
        result = encode_apache(data)
        self.assertIn("key value", result)

    def test_encode_erlang(self):
        data = {"key": "value"}
        result = encode_erlang(data)
        self.assertIn("{key, value}", result)

    def test_encode_haproxy(self):
        data = [{"section": ["param1", "param2"]}]
        result = encode_haproxy(data)
        self.assertIn("section", result)
        self.assertIn("param1", result)

    def test_encode_ini(self):
        data = {"section": {"key": "value"}}
        result = encode_ini(data)
        self.assertIn("[section]", result)
        self.assertIn("key=value", result)

    def test_encode_json(self):
        data = {"key": "value"}
        result = encode_json(data)
        self.assertIn('"key": "value"', result)

    def test_encode_logstash(self):
        data = {"key": "value"}
        result = encode_logstash(data)
        self.assertIn('"key": "value"', result)
