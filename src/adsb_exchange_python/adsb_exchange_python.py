import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import logging
from typing import Dict

logger = logging.getLogger(__name__)

class AdsbExchangeAPI:
    """
    A minimal wrapper for the Basic ADS-B Exchange API
    """

    BASE_URL = "https://adsbexchange-com1.p.rapidapi.com/v2"
    HOST = "adsbexchange-com1.p.rapidapi.com"

    def __init__(self, api_key: str, max_retries: int = 3):
        """
        Initialize the API wrapper with your RapidAPI key.

        :param api_key: Your RapidAPI key for the ADS-B Exchange API.
        :param max_retries: The maximum number of retries for failed requests.
        """
        self.session = requests.Session()
        self.session.headers.update({
            "x-rapidapi-key": api_key,
            "x-rapidapi-host": self.HOST
        })
        retries = Retry(
            total=max_retries,
            backoff_factor=0.1,
            status_forcelist=[500, 502, 503, 504],
            allowed_methods=["GET"]
        )
        adapter = HTTPAdapter(max_retries=retries)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)

    def _get(self, endpoint: str) -> Dict:
        """
        Internal method to perform GET requests to the API.

        :param endpoint: The API endpoint to query.
        :return: JSON response from the API.
        :raises requests.exceptions.HTTPError: If the HTTP request returned an unsuccessful status code.
        """
        url = f"{self.BASE_URL}{endpoint}"
        logger.debug(f"Making GET request to {url}")
        try:
            response = self.session.get(url)
            response.raise_for_status()
            json_data = response.json()
            logger.debug(f"Received response: {json_data}")
            return json_data
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTPError for URL {url}: {e}")
            raise
        except ValueError as e:
            logger.error(f"Failed to parse JSON response from {url}: {e}")
            raise

    def get_by_registration(self, registration: str) -> Dict:
        """
        Get single aircraft position by registration.

        :param registration: The aircraft registration number (e.g., "N8737L").
        :return: JSON data for the specified registration.
        
        Example:
            >>> api = AdsbExchangeAPI(api_key="YOUR_API_KEY")
            >>> data = api.get_by_registration("N8737L")
            >>> print(data)
        """
        endpoint = f"/registration/{registration}/"
        return self._get(endpoint)

    def get_by_icao(self, icao: str) -> Dict:
        """
        Get single aircraft position by ICAO Mode S 6-digit transponder hex code.

        :param icao: The ICAO address (hex) of the aircraft (e.g., "a4b065").
        :return: JSON data for the specified ICAO code.
        
        Example:
            >>> data = api.get_by_icao("a4b065")
            >>> print(data)
        """
        endpoint = f"/icao/{icao}/"
        return self._get(endpoint)

    def get_by_hex(self, hex_code: str) -> Dict:
        """
        Get last known location of an aircraft using the mode-s hex (icao).

        :param hex_code: The hex code of the aircraft (e.g., "a4b605").
        :return: JSON data for the specified hex code.
        
        Example:
            >>> data = api.get_by_hex("a4b605")
            >>> print(data)
        """
        endpoint = f"/hex/{hex_code}/"
        return self._get(endpoint)

    def get_by_callsign(self, callsign: str) -> Dict:
        """
        Get aircraft currently broadcasting a specific call sign.

        :param callsign: The callsign of the aircraft (e.g., "NKS185").
        :return: JSON data for the specified callsign.
        
        Example:
            >>> data = api.get_by_callsign("NKS185")
            >>> print(data)
        """
        endpoint = f"/callsign/{callsign}/"
        return self._get(endpoint)

    def get_by_squawk(self, squawk: str) -> Dict:
        """
        Get aircraft currently broadcasting a specific squawk code.

        :param squawk: The squawk code (e.g., "1200").
        :return: JSON data for the specified squawk code.
        
        Example:
            >>> data = api.get_by_squawk("1200")
            >>> print(data)
        """
        endpoint = f"/sqk/{squawk}/"
        return self._get(endpoint)

    def get_military_aircraft(self) -> Dict:
        """
        Get all active aircraft tagged as military.

        :return: JSON data for military aircraft.
        
        Example:
            >>> data = api.get_military_aircraft()
            >>> print(data)
        """
        endpoint = "/mil/"
        return self._get(endpoint)

    def get_nearby(self, lat: float, lon: float, dist: float) -> Dict:
        """
        Get all aircraft within a specified distance up to 250 NM.

        :param lat: Latitude of the location.
        :param lon: Longitude of the location.
        :param dist: Distance in nautical miles to search within.
        :return: JSON data for aircraft within the specified area.
        :raises ValueError: If dist is greater than 250 NM.
        
        Example:
            >>> data = api.get_nearby(37.7749, -122.4194, 100)
            >>> print(data)
        """
        if dist > 250:
            raise ValueError("Distance must be 250 NM or less.")
        endpoint = f"/lat/{lat}/lon/{lon}/dist/{dist}/"
        return self._get(endpoint)
