#pip install speedtest-cli
import speedtest as sp
import sys

test = sp.Speedtest()

down = test.download()
rsDown = round(down)
fDown = int(rsDown/1e+6)

upload = test.upload()
rsUp = round(upload)
fUp=int(rsUp/1e+6)

print(f"Down:{fDown} mb/Up:{fUp} mb")

