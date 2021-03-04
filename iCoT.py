import location
import time
import console
from datetime import datetime, timedelta
import xmltodict
import socket
import configparser

console.clear()
console.show_activity()

def main():
	config = configparser.ConfigParser()
	config.read("iCoT.conf")
	print('Sending iCoT data to {}:{}'.format(config['metadata']['takip'],int(config['metadata']['takport'])))
	try:
		while True:
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			sock.sendto(
				bytes(locater(config), 'utf-8'), (config['metadata']['takip'],int(config['metadata']['takport'])))
			sock.close()
			time.sleep(int(config['metadata']['refresh']))
	except Exception as e:  # If we hit an issue, try to close the connection
		print(f'iCoT service stopped unexpectedly: {e}')
		sock.close()


def locater(config):  # Generates XML CoT message

	# Generate some admin data

	location.start_updates()
	loc = location.get_location()
	data = {}
	data['event'] = {}
	data['event']['point'] = {}
	data['event']['detail'] = {}
	data['event']['detail']['contact'] = {}
	now = datetime.utcnow()
	stale = now + timedelta(minutes=10)

	# Event Data 

	data['event']['@version'] = '2.0'
	data['event']['@uid'] = config['metadata']['uid']
	data['event']['@type'] = config['metadata']['type']
	data['event']['@time'] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
	data['event']['@start'] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
	data['event']['@stale'] = stale.strftime("%Y-%m-%dT%H:%M:%SZ")
	data['event']['@how'] = config['metadata']['how']

	# Point data

	data['event']['point']['@lat'] = str(loc['latitude'])
	data['event']['point']['@lon'] = str(loc['longitude'])
	data['event']['point']['@hae'] = str(loc['altitude'])
	data['event']['point']['@ce'] = str(loc['horizontal_accuracy'])
	data['event']['point']['@le'] = str(loc['vertical_accuracy'])

	# Detail data

	data['event']['detail']['contact']['@callsign'] = config['metadata'][
		'callsign']

	# Convert dict to XML

	data = xmltodict.unparse(data)

	return data

main()
