import logging
from adsb_exchange_python import AdsbExchangeAPI

def main():
    # Configure logging to display debug messages from the API wrapper
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    # Replace 'YOUR_RAPIDAPI_KEY' with your actual RapidAPI key
    api_key = 'YOUR_RAPIDAPI_KEY'
    api = AdsbExchangeAPI(api_key=api_key)

    # Test get_by_registration
    registration = 'N8737L'
    try:
        registration_data = api.get_by_registration(registration)
        logger.info(f"Data for registration {registration}:")
        logger.info(registration_data)
    except Exception as e:
        logger.error(f"Error fetching data for registration {registration}: {e}")

    # Test get_by_icao
    icao = 'a4b065'
    try:
        icao_data = api.get_by_icao(icao)
        logger.info(f"Data for ICAO {icao}:")
        logger.info(icao_data)
    except Exception as e:
        logger.error(f"Error fetching data for ICAO {icao}: {e}")

    # Test get_by_hex
    hex_code = 'a4b605'
    try:
        hex_data = api.get_by_hex(hex_code)
        logger.info(f"Data for hex code {hex_code}:")
        logger.info(hex_data)
    except Exception as e:
        logger.error(f"Error fetching data for hex code {hex_code}: {e}")

    # Test get_by_callsign
    callsign = 'NKS185'
    try:
        callsign_data = api.get_by_callsign(callsign)
        logger.info(f"Data for callsign {callsign}:")
        logger.info(callsign_data)
    except Exception as e:
        logger.error(f"Error fetching data for callsign {callsign}: {e}")

    # Test get_by_squawk
    squawk = '1200'
    try:
        squawk_data = api.get_by_squawk(squawk)
        logger.info(f"Data for squawk code {squawk}:")
        logger.info(squawk_data)
    except Exception as e:
        logger.error(f"Error fetching data for squawk code {squawk}: {e}")

    # Test get_military_aircraft
    try:
        military_data = api.get_military_aircraft()
        logger.info("Military aircraft data:")
        logger.info(military_data)
    except Exception as e:
        logger.error(f"Error fetching military aircraft data: {e}")

    # Test get_nearby
    lat, lon, dist = 51.46888, -0.45390, 250  # Coordinates near London Heathrow Airport
    try:
        nearby_data = api.get_nearby(lat=lat, lon=lon, dist=dist)
        logger.info(f"Aircraft near latitude {lat}, longitude {lon}, within {dist} NM:")
        logger.info(nearby_data)
    except ValueError as ve:
        logger.error(f"ValueError: {ve}")
    except Exception as e:
        logger.error(f"Error fetching nearby aircraft data: {e}")

if __name__ == '__main__':
    main()
