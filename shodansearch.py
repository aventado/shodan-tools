#shodan basic search

import shodan
import sys
from ConfigParser import ConfigParser

#grab the api key from auth.ini
config = ConfigParser()
config.read('auth.ini')
SHODAN_API_KEY = config.get('auth','API_KEY')

#initialize the api object
api = shodan.Shodan(SHODAN_API_KEY)

# Input validation
if len(sys.argv) == 1:
        print 'Usage: %s <search query>' % sys.argv[0]
        sys.exit(1)

try:

        # Perform the search
        query = ' '.join(sys.argv[1:])
        result = api.search(query)

        # Loop through the matches and print each IP
        for service in result['matches']:
                print service['ip_str']
except Exception, e:
        print 'Error: %s' % e
        sys.exit(1)
