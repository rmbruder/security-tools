import urllib.request
import re
import argparse


parser=argparse.ArgumentParser()

parser.add_argument('url_path', help='Provide a URL as an argument')

args=parser.parse_args()


with urllib.request.urlopen(args.url_path) as response:
   html = response.read()


linklist = re.findall(r'(?i)href=["\'].*?["\']',html.decode())

for link in linklist:
   print(link)


