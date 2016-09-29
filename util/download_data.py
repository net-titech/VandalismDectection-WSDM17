from sys import argv
from urllib.request import urlopen

def main():
    months = [str(x).zfill(2) for x in range(1,13)]
    years = [str(x) for x in range(2012, 2017)]
    rooturl = 'http://www.uni-weimar.de/medien/webis/corpora/corpus-wdvc-16/'
    rootname = 'wdvc16_'
    ext = '.xml.7z'
    directory = '../data/'
    if len(argv) == 5:
        _, rooturl, rootname, ext, directory = argv
    for year in years:
        for month in months:
            request_url = rooturl + rootname + year + '_' + month + ext
            try:
                print('Downloading', rootname + year + '_' + month + ext)
                with urlopen(request_url) as response:
                  data = response.read()
                with open(directory+rootname+year+'_'+month+ext, 'wb') as f:
                    f.write(data)
                    print('Write ' + rootname+year+'_'+month+ext, 'wb')
                print('Success!')
            except:
                print('Failed')
                continue

if __name__ == '__main__':
    main()
