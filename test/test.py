# standard
import sys
import time

def test_mcutil():
    #from mccpy.mccutil import MccUtil
    from mccutil import MccUtil

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'}
    MccUtil.download(headers, '.', 'be')


def test_mccmanager():
    #from mccpy.mccmanager import MccManager
    from mccmanager import MccManager

    mm = MccManager()
    mm.start(r".\bin\bedrock-server-1.19.73.02\bedrock_server.exe")
    time.sleep(20)
    mm.stop()


def main():
    sys.path.append('mccpy')
    test_mcutil()
    test_mccmanager()


if __name__ == '__main__':
    main()

