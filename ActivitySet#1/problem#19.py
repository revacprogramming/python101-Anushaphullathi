#Json
import json
import urllib.request, urllib.parse, urllib.error
sum = 0
fhand = urllib.request.uropen('http://py4e-data.dr-chuck.net/comments_42.json')
info = json.loads(fhand)
print('User count:', len(info))
for item in info:
    sum = info.
    sum+=sum
print(sum)


