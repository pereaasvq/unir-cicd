import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs

@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        result = response.read().decode('utf-8')
        self.assertEqual(result, "4", f"Resultado incorrecto para {url}")

    def test_api_add_invalid(self):
        url = f"{BASE_URL}/calc/add/2/abc"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")
            error_message = e.read().decode('utf-8')
            self.assertIn("Operator cannot be converted to number", error_message)
        else:
            self.fail(f"Expected HTTPError not raised for {url}")

    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/5/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        result = response.read().decode('utf-8')
        self.assertEqual(result, "2", f"Resultado incorrecto para {url}")

    def test_api_substract_invalid(self):
        url = f"{BASE_URL}/calc/substract/5/abc"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")
            error_message = e.read().decode('utf-8')
            self.assertIn("Operator cannot be converted to number", error_message)
        else:
            self.fail(f"Expected HTTPError not raised for {url}")

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/3/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        result = response.read().decode('utf-8')
        self.assertEqual(result, "12", f"Resultado incorrecto para {url}")

    def test_api_multiply_invalid(self):
        url = f"{BASE_URL}/calc/multiply/3/abc"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")
            error_message = e.read().decode('utf-8')
            self.assertIn("Operator cannot be converted to number", error_message)
        else:
            self.fail(f"Expected HTTPError not raised for {url}")

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/10/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        result = response.read().decode('utf-8')
        self.assertEqual(result, "5.0", f"Resultado incorrecto para {url}")

    def test_api_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/10/0"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")
            error_message = e.read().decode('utf-8')
            self.assertIn("Division by zero is not possible", error_message)
        else:
            self.fail(f"Expected HTTPError not raised for {url}")

    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        result = response.read().decode('utf-8')
        self.assertEqual(result, "8", f"Resultado incorrecto para {url}")

    def test_api_power_invalid(self):
        url = f"{BASE_URL}/calc/power/2/abc"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")
            error_message = e.read().decode('utf-8')
            self.assertIn("Operator cannot be converted to number", error_message)
        else:
            self.fail(f"Expected HTTPError not raised for {url}")

    def test_api_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/16"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        result = response.read().decode('utf-8')
        self.assertEqual(result, "4.0", f"Resultado incorrecto para {url}")

    def test_api_sqrt_invalid(self):
        url = f"{BASE_URL}/calc/sqrt/abc"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")
            error_message = e.read().decode('utf-8')
            self.assertIn("Operator cannot be converted to number", error_message)
        else:
            self.fail(f"Expected HTTPError not raised for {url}")

    def test_api_log10(self):
        url = f"{BASE_URL}/calc/log10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        result = response.read().decode('utf-8')
        self.assertEqual(result, "2.0", f"Resultado incorrecto para {url}")

    def test_api_log10_invalid(self):
        url = f"{BASE_URL}/calc/log10/abc"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")
            error_message = e.read().decode('utf-8')
            self.assertIn("Operator cannot be converted to number", error_message)
        else:
            self.fail(f"Expected HTTPError not raised for {url}")

    def test_api_log10_non_positive(self):
        url = f"{BASE_URL}/calc/log10/0"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")
            error_message = e.read().decode('utf-8')
            self.assertIn("Logarithm only defined for positive numbers", error_message)
        else:
            self.fail(f"Expected HTTPError not raised for {url}")

        url = f"{BASE_URL}/calc/log10/-10"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")
            error_message = e.read().decode('utf-8')
            self.assertIn("Logarithm only defined for positive numbers", error_message)
        else:
            self.fail(f"Expected HTTPError not raised for {url}")
