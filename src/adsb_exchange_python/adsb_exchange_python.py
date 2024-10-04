# src/adsb_exchange_python/adsb_exchange_python.py

import requests

class AdsbExchangeAPI:
    """
    A minimal wrapper for the Basic ADS-B Exchange API
    """

    BASE_URL = "https://adsbexchange-com1.p.rapidapi.com/v2"
    HOST = "adsbexchange-com1.p.rapidapi.com"

    def __init__(self, api_key):
        """
        Initialize the API wrapper with your RapidAPI key.

        :param api_key: Your RapidAPI key for the ADS-B Exchange API.
        """
        self.headers = {
            "x-rapidapi-key": api_key,
            "x-rapidapi-host": self.HOST
        }

    def _get(self, endpoint):
        """
        Internal method to perform GET requests to the API.

        :param endpoint: The API endpoint to query.
        :return: JSON response from the API.
        :raises requests.exceptions.HTTPError: If the HTTP request returned an unsuccessful status code.
        """
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()

    def get_by_registration(self, registration):
        """
        Get single aircraft position by registration.

        :param registration: The aircraft registration number (e.g., "N8737L").
        :return: JSON data for the specified registration.
        """
        endpoint = f"/registration/{registration}/"
        return self._get(endpoint)

    def get_by_icao(self, icao):
        """
        Get single aircraft position by ICAO mode S 6-digit transponder hex code (if currently tracked).

        :param icao: The ICAO address (hex) of the aircraft (e.g., "a4b065").
        :return: JSON data for the specified ICAO code.
        """
        endpoint = f"/icao/{icao}/"
        return self._get(endpoint)

    def get_by_hex(self, hex_code):
        """
        Get one aircraft last known location using the mode-s hex (icao), if aircraft has flown in the last 48 hours.

        :param hex_code: The hex code of the aircraft (e.g., "a4b605").
        :return: JSON data for the specified hex code.
        """
        endpoint = f"/hex/{hex_code}/"
        return self._get(endpoint)

    def get_by_callsign(self, callsign):
        """
        Get one or more aircraft currently broadcasting a call sign.

        :param callsign: The callsign of the aircraft (e.g., "NKS185").
        :return: JSON data for the specified callsign.
        """
        endpoint = f"/callsign/{callsign}/"
        return self._get(endpoint)

    def get_by_squawk(self, squawk):
        """
        Get one or more aircraft currently broadcasting a specific squawk code.

        :param squawk: The squawk code (e.g., "1200").
        :return: JSON data for the specified squawk code.
        """
        endpoint = f"/sqk/{squawk}/"
        return self._get(endpoint)

    def get_military_aircraft(self):
        """
        Get all active aircraft tagged as military.

        :return: JSON data for military aircraft.
        """
        endpoint = "/mil/"
        return self._get(endpoint)

    def get_nearby(self, lat, lon, dist):
        """
        Get all aircraft within specified distance up to 250 NM.

        :param lat: Latitude of the location.
        :param lon: Longitude of the location.
        :param dist: Distance in nautical miles to search within.
        :return: JSON data for aircraft within the specified area.
        """
        endpoint = f"/lat/{lat}/lon/{lon}/dist/{dist}/"
        return self._get(endpoint)
