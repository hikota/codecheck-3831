#!/usr/bin/env python3
def main(argv):
  str = ""
  for v in argv:
    if not v.isdigit():
      str = "invalid"
    elif int(v) % 3 == 0 and "3" not in v:
      str = "idiot"
    elif "3" in v:
      if int(v) % 3 == 0:
        str = "dumb"
      else:
        str = "stupid"
    else:
      str = "smart"
    print(str)