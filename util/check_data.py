from urllib.request import urlopen
from hashlib import md5
from os import listdir
from os.path import isfile

# Load md5 list as string and compare with local files' hashes.
def main():
    md5_url = 'http://www.uni-weimar.de/medien/webis/corpora/corpus-wdvc-16/checksums.md5'
    data_dir = '../data/'
    data_files = [f for f in listdir(data_dir)]
    with urlopen(md5_url) as response:
        md5list = response.read()
    md5string = md5list.decode()
    md5dict = {}
    for data in md5string.splitlines():
        md5str, fname = data.split()
        md5dict[fname[1:]] = md5str
    for filename in data_files:
        try:
            if md5dict[filename] == filemd5(data_dir+filename):
                print(filename, 'Passed.')
            else:
                print('Please recheck', filename)
        except:
            print(filename, 'not found.')

# Read file and return md5 hash as string
def filemd5(fname):
    hash_md5 = md5()
    with open(fname, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

if __name__ == '__main__':
    main()
