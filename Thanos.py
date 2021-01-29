#! /usr/bin/env python3

import os
import os.path

import random
import sys

GEMS = ["Space", "Time", "Reality", "Soul", "Mind", "Power"] # Thanos necesita las 6 gemas para tener el poder de matar a la mitad de tus archivos

class Thanos:

    def __init__(self, *gems):
        self.gems = gems

    def snap(self, folder):

        for path in os.listdir(folder):
            path = os.path.join(folder, path)
            value = random.random()
            if value < 0.5:
                os.remove(path)
                print(path + " ... is gone")
                pass
            
if __name__ == "__main__":
    arg = sys.argv
    if "--gauntlet" in sys.argv[2:] and "--infinity-gems" in sys.argv[2:]:
        Thanos(GEMS).snap(sys.argv[1])    
