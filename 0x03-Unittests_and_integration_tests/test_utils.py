#!/usr/bin/env python3
""" Unittest for access_nested_map """
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TetstAccessNestedMap(unittest.TestCase):
    """ test class """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """ test the function returns expected output """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_output)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_output):
        """ test the function raises exception """
        with self.assertRaises(expected_output) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ tests the get_json function """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """ test get_json returns expected result """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch("requests.get", return_value=mock_response) as mock_request:
            response = get_json(test_url)
            mock_request.assert_called_once_with(test_url)
            self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """ tests the memoize decorator """
    def test_memoize(self):
        class TestClass:
            """ test class """
            def a_method(self):
                """ retunrs 42 """
                return 42

            @memoize
            def a_property(self):
                """ calls a_method and returns the value """
                return self.a_method()

        test_obj = TestClass()
        with patch.object(test_obj, "a_method") as mock_method:
            mock_method.return_value = 42
            self.assertEqual(test_obj.a_property, 42)
            self.assertEqual(test_obj.a_property, 42)
            mock_method.assert_called_once()
