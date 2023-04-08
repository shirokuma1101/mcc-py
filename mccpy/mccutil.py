# standard
import os
import subprocess
from urllib.parse import urlparse

# scraping
import requests
from bs4 import BeautifulSoup


class MccUtil:

    # public

    def __init__(self) -> None:
        pass

    @staticmethod
    def download(headers: dict, download_dir: str, edition: str, platform: str = 'win', version: str = None) -> bool:
        dir_url = MccUtil._getmcurl(headers=headers, edition=edition, platform=platform, version=version)
        if dir_url:
            res = requests.get(dir_url, headers=headers)
            if res.ok:
                with open(f'{download_dir}/{os.path.basename(urlparse(dir_url).path)}', 'wb') as f:
                    f.write(res.content)
                return True

        return False

    @staticmethod
    def getstdout(proc: subprocess.Popen, encoding: str='utf-8') -> str:
        while True:
            line = proc.stdout.readline()
            if not line:
                break
            yield line.decode(encoding).strip()

    @staticmethod
    def inputstdin(cmd: str, proc: subprocess.Popen, encodeing: str='utf-8', nc: str='\r\n') -> None:
        proc.stdin.write(f'{cmd}{nc}'.encode(encodeing))
        proc.stdin.flush()

    # private
    @staticmethod
    def _getmcurl(headers: dict, edition: str, platform: str = 'win', version: str = None) -> str:
        if edition == 'je':
            pass
        elif edition == 'be':
            mc_url = 'https://www.minecraft.net/en-us/download/server/bedrock'
            res = requests.get(mc_url, headers=headers)
            if res.ok:
                soup = BeautifulSoup(res.text, 'html.parser')
                if platform == 'win':
                    soup = soup.find('a', {'data-platform': f'serverBedrockWindows'})
                elif platform == 'linux':
                    soup = soup.find('a', {'data-platform': f'serverBedrockLinux'})
                return soup.get('href')

        return None

