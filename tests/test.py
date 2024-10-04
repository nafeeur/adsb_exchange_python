# test.py

from adsb_exchange_python import AdsbExchangeAPI

def main():
    # Replace 'YOUR_RAPIDAPI_KEY' with your actual RapidAPI key
    api_key = 'YOUR_RAPIDAPI_KEY'
    api = AdsbExchangeAPI(api_key=api_key)

    # Test get_by_registration
    registration = 'N8737L'
    try:
        registration_data = api.get_by_registration(registration)
        print(f"\nData for registration {registration}:")
        print(registration_data)
    except Exception as e:
        print(f"Error fetching data for registration {registration}: {e}")

    # Test get_by_icao
    icao = 'a4b065'
    try:
        icao_data = api.get_by_icao(icao)
        print(f"\nData for ICAO {icao}:")
        print(icao_data)
    except Exception as e:
        print(f"Error fetching data for ICAO {icao}: {e}")

    # Test get_by_hex
    hex_code = 'a4b605'
    try:
        hex_data = api.get_by_hex(hex_code)
        print(f"\nData for hex code {hex_code}:")
        print(hex_data)
    except Exception as e:
        print(f"Error fetching data for hex code {hex_code}: {e}")

    # Test get_by_callsign
    callsign = 'NKS185'
    try:
        callsign_data = api.get_by_callsign(callsign)
        print(f"\nData for callsign {callsign}:")
        print(callsign_data)
    except Exception as e:
        print(f"Error fetching data for callsign {callsign}: {e}")

    # Test get_by_squawk
    squawk = '1200'
    try:
        squawk_data = api.get_by_squawk(squawk)
        print(f"\nData for squawk code {squawk}:")
        print(squawk_data)
    except Exception as e:
        print(f"Error fetching data for squawk code {squawk}: {e}")

    # Test get_military_aircraft
    try:
        military_data = api.get_military_aircraft()
        print("\nMilitary aircraft data:")
        print(military_data)
    except Exception as e:
        print(f"Error fetching military aircraft data: {e}")

    # Test get_nearby
    lat, lon, dist = 51.46888, -0.45390, 250  # Coordinates near London Heathrow Airport
    try:
        nearby_data = api.get_nearby(lat=lat, lon=lon, dist=dist)
        print(f"\nAircraft near latitude {lat}, longitude {lon}, within {dist} nautical miles:")
        print(nearby_data)
    except Exception as e:
        print(f"Error fetching nearby aircraft data: {e}")

if __name__ == '__main__':
    main()
