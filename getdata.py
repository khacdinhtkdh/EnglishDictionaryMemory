import requests
from bs4 import BeautifulSoup

link = 'https://dictionary.cambridge.org/vi/dictionary/english/'
cambride = "https://dictionary.cambridge.org/"

headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'My User Agent 1.0',
    })


def download_mp3(word):
    ld = None
    pro = ""
    r = requests.get(link + word, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    for a in soup.find_all('amp-audio'):
        filename = a.find_all('source')
        for f in filename:
            attr = f.attrs['src']
            if 'us_pron' in attr and 'mp3' in attr:
                ld = attr
        if ld is not None:
            break
    if ld is None:
        return False, pro

    for a in soup.find_all(class_="pron dpron"):
        if 'us' in a.parent.text:
            pro = a.text
            break

    with requests.Session() as req:
        download = req.get(cambride + ld, headers=headers)
        if download.status_code == 200:
            with open('download.mp3', 'wb') as f:
                f.write(download.content)
                f.close()
        else:
            print(f"Download Failed For File")
            return False, pro
    return True, pro


def download_pron_dpron(word):
    r = requests.get(link + word, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    for a in soup.find_all(class_="pron dpron"):
        if 'us' in a.parent.text:
            return a.text
    return ""
