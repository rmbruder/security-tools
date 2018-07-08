import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'http://ip.42.pl/raw')
publicIP = r.data
print("Your public IP address is: {}".format(publicIP))

