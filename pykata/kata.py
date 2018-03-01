"""
Module for launching this day kata
"""

from datetime import date
import importlib
import sys

def main():
    module_name = "pykata.daily.day" + date.today().strftime("%Y%m%d")
    if len(sys.argv) > 1:
        module_name = sys.argv[1]
    m = importlib.import_module(module_name)
    m.kata()
    m.retro()
    

if __name__ == "__main__":
    main()