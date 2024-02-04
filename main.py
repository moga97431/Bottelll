import requests

print('Beginning file download with requests')

url =input('')
r = requests.get(url)

with open('video.mp3', 'wb') as f:
    f.write(r.content)

# Retrieve HTTP meta-data
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
