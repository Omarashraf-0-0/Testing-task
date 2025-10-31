import unittest
from unittest.mock import patch, Mock
import requests
from employeeRepository import EmployeeRepository


class EmployeeRepositoryTests(unittest.TestCase):

    def setUp(self):
        self.repo = EmployeeRepository("http://dummy-api.com/employees")

        self.rawEmployees = [
            {"id": 3, "name": "Alice", "position": "Developer"},
            {"id": 1, "name": "Bob", "position": "Manager"},
            {"id": 2, "name": "Charlie", "position": "Designer"}
        ]

        self.expectedSorted = [
            {"id": 1, "name": "Bob", "position": "Manager"},
            {"id": 2, "name": "Charlie", "position": "Designer"},
            {"id": 3, "name": "Alice", "position": "Developer"}
        ]

    @patch("employeeRepository.requests.get")
    def test_fetchEmployees_successAndSorted(self, mockGet):
        mockResponse = Mock()
        mockResponse.ok = True
        mockResponse.json.return_value = self.rawEmployees
        mockGet.return_value = mockResponse

        employees = self.repo.fetchEmployees()

        mockGet.assert_called_once_with("http://dummy-api.com/employees", timeout=5)
        self.assertEqual(employees, self.expectedSorted)
        print("✅ Test 1 (Success & Sorting) Passed")

    @patch("employeeRepository.requests.get")
    def test_fetchEmployees_serverError(self, mockGet):
        mockResponse = Mock()
        mockResponse.ok = False
        mockGet.return_value = mockResponse

        employees = self.repo.fetchEmployees()
        self.assertIsNone(employees)
        print("✅ Test 2 (Server Error) Passed")

    @patch("employeeRepository.requests.get")
    def test_fetchEmployees_networkFailure(self, mockGet):
        mockGet.side_effect = requests.RequestException

        employees = self.repo.fetchEmployees()
        self.assertIsNone(employees)
        print("✅ Test 3 (Network Failure) Passed")


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
