import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry


class ApiError(Exception):
    """Route various errors into one class - for readability"""
    pass


class ApiClient:
    """Make GET requests to an API endpoint, expect JSON response."""
    
    
    def __init__(self, 
                 base_url, 
                 headers=None, 
                 auth=None, 
                 timeout=(3),
                 retries=3
                 ):
        """Create client with session and retry policy"""

        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(headers or {})
        self.session.auth = auth
        self.session.mount("https://", HTTPAdapter(max_retries=Retry(
            total=retries,
            backoff_factor=0.5,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods={"GET"}
        )))


    def get_json(self, path, params=None):
        """Send a GET request and return JSON response"""

        url = f"{self.base_url}/{path.lstrip("/")}"

        try:
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.HTTPError as exc:
            if exc.response is not None:
                raise ApiError(f"{url} returned {exc.response.status_code}") from exc
            raise ApiError(f"{url} return a http error")
        except requests.exceptions.RequestException as exc:
            raise ApiError(f"{url} ran into an issue")
        except:
            raise ApiError("Something went wrong with get_json :(")



