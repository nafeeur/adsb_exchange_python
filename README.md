# ADS-B Exchange API Wrapper

A minimal Python wrapper for the ADS-B Exchange API, enabling easy access to real-time aircraft data.

https://rapidapi.com/adsbx/api/adsbexchange-com1

## Installation

Install the package via pip:

```bash
pip3 install adsb-exchange-python
```
## Usage 
```python
from adsb_exchange import AdsbExchangeAPI

# Replace 'YOUR_RAPIDAPI_KEY' with your actual RapidAPI key
api_key = 'YOUR_RAPIDAPI_KEY'
api = AdsbExchangeAPI(api_key=api_key)

# Get aircraft data by registration
data = api.get_by_registration('N8737L')
print(data)
```
