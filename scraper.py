import requests
import json

chapter = input("Enter chapter to download: ")
path = input("Enter path were to store downloaded files: ")

headers = {
    'authority': 'attackontitanread.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://attackontitanread.com/manga/attack-on-titan-chapter-[chapter]-online-read/',
    'accept-language': 'en-US,en;q=0.9,ka;q=0.8',
    'cookie': '__cfduid=d37d007a15808a7143c63064f5d961a451617389633',
}

headers = json.dumps(headers)

headers = headers.replace('[chapter]', chapter)

headers = json.loads(headers)

response = requests.get(
    'https://attackontitanread.com/manga/attack-on-titan-chapter-' + chapter + '-online-read/', headers=headers)


print(str(response.content).count("<img src=")) #count number of images

number_of_images = str(response.content).count("<img src=")

headers2 = {
    'authority': 'read.mangadad.com',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-dest': 'image',
    'referer': 'https://attackontitanread.com/',
    'accept-language': 'en-US,en;q=0.9,ka;q=0.8',
}

req_str = 'https://read.mangadad.com/Mangadad/attack-on-titan/chapter-130/[count].jpg' #replacement string

for i in range (1, int(number_of_images) + 1): #Downloading images
    x = req_str.replace('[count]', str(i))
    response2 = requests.get(x, headers=headers2, allow_redirects=True)
    open(path + str(i) + '.jpg', 'wb').write(response2.content)
