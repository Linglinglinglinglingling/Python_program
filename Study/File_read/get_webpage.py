import urllib.request
url='http://users.monash.edu/~guidot/test.html'
# file_name='test_get_webpage.txt'
# urllib.request.urlretrieve(url,file_name)

a=urllib.request.urlopen(url)
b=str(a.re)
