
import sys
import os
import re
import shutil

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 mklatest.py <folder>")
        return

    print("finding latest in: " + sys.argv[1])
    files = os.listdir(sys.argv[1])

    version = 0

    for file in files:
        x = re.match(r"^v([0-9]+)\.json",file)
        if x != None:
            v = x.group(1)
            if int(v) > version:
                version = int(v)

    print("copying latest to: " + sys.argv[1]+"/latest.json")
    shutil.copyfile(sys.argv[1] + f"/v{version}.json",
                    sys.argv[1] + "/latest.json")


if __name__ == "__main__":
    main()