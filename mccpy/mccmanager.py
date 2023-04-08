# standard
import subprocess
import threading

# mccutil
from mccutil import MccUtil


class MccManager:

    # public

    def __init__(self) -> None:
        self.mc_process = None
        self.mc_thread = None

    def start(self, start_path: str, encoding: str='utf-8') -> None:
        self.mc_process = subprocess.Popen(start_path,
                                           stdin=subprocess.PIPE,
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.STDOUT,
                                           shell=True)
        def log() -> None:
            for line in MccUtil.getstdout(self.mc_process, encoding=encoding):
                print(line)
                #todo parse and write to log

        self.mc_thread = threading.Thread(target=log)
        self.mc_thread.start()

    def stop(self) -> None:
        MccUtil.inputstdin('stop', self.mc_process)
        self.mc_thread.join()

