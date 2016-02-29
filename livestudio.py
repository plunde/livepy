import urllib
import re
import webbrowser
from BeautifulSoup import *

# Input prompt
url = raw_input('Enter URL: ')
if len(url) < 1 : url = "http://fvndirekte.kinsta.com/sorlandet-live-onsdag-17-februar/"
print 'Fetching Engage links for FVN.no articles...'
	
try:
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
except:
	print 'Oops! Did you include "http://"?'
	quit()

count = 0

#Find FVN.no articles, extract article ID and insert into Engage link
for elem in soup.findAll('a', href=re.compile('http://www\.fvn\.no/')):
	elemstr = str(elem)
	xline = re.findall('(\d+).html', elemstr)
	for i in xline:
		url = 'https://engage.schibsted.media/article-details/'+xline[0]+'/views'
		print url
		#webbrowser.open_new_tab(url)
		count += 1

print 'Found', count, 'links.'
print 'Done.'



