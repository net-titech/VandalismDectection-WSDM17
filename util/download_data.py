from sys import argv
from urllib2 import openurl
from urllib2 import HTTPError

months = [str(x).zfill(2) for x in range(1,13)]
years = [str(x) for x in range(2012, 2017)]
rooturl = 'http://www.uni-weimar.de/medien/webis/corpora/corpus-wdvc-16/'
rootname = 'wdvc16_'
ext = '.xml.7z'

def main():
    if len(argv) > 1:
        _, rooturl, ext = argv
    print('Downloading data...')
    for year in years:
        for month in months:
            request_url = rooturl + year + '_' + month + ext
            try:
                data = openurl(request_url)
                with open(rootname+year+'_'+month+ext, 'wb') as f:
                    f.write(data)
            except HTTPError:
                continue

if __name__ == '__main__':
    main()


