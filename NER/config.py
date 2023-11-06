import get_data.helper as helper

config = helper.read_config()

username = config['GEONAMESSettings']['username']

print("\nDisplaying Access details\n")

print("GEONAMES Username: " + username)