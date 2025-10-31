import requests

class EmployeeRepository:
    def __init__(self, apiUrl):
        self.apiUrl = apiUrl

    def fetchEmployees(self):
        """
        Fetch employees from API and return a sorted list by ID.
        Returns None if API call fails or response is invalid.
        """
        try:
            res = requests.get(self.apiUrl, timeout=5)
            if not res.ok:
                return None

            data = res.json()
            if not isinstance(data, list):
                return None

            # Sort employees by ID safely
            return sorted(data, key=lambda emp: emp.get("id", float('inf')))

        except (requests.RequestException, ValueError, KeyError):
            return None
