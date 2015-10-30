#example script for shodan.io
#Joshua Harper

import shodan
from ConfigParser import ConfigParser

#grab the api key from auth.ini
config = ConfigParser()
config.read('auth.ini')
SHODAN_API_KEY = config.get('auth','API_KEY')

#initialize the api object
api = shodan.Shodan(SHODAN_API_KEY)

# Wrap the request in a try/ except block to catch errors
try:
        # Search Shodan
        results = api.search('linksys')

        # Show the results
        print 'Results found: %s' % results['total']
        for result in results['matches']:
                print 'IP: %s' % result['ip_str']
                print result['data']
                print ''
except shodan.APIError, e:
        print 'Error: %s' % e
