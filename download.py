from datetime import datetime
from tqdm import tqdm
import requests
import re
import os

def main(lista,html):
    try:
        if len(lista) == 2:
            if 0 in lista and 1 in lista:
                try:
                    # intenta bajar HD
                    download_video("HD",html)
                    return True

                except Exception as e:
                    print(e)
                    # intenta bajar SD
                    download_video("SD",html)
                    return True

    except:
        print("Error en main")


def download_video(quality,html):
    print(f"Bajando video en {quality}\n")
    video_url = re.search(rf'{quality.lower()}_src:"(.+?)"', html).group(1)
    file_size_request = requests.get(video_url, stream=True)
    file_size = int(file_size_request.headers['Content-Length'])
    block_size = 1024
    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
    t = tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
    with open(filename + '.mp4', 'wb') as f:
        for data in file_size_request.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()
    print("\nVideo Descragado.")
    return True


def face_video(url):
    try:
        html = requests.get(url).content.decode('utf-8')


        _qualityhd = re.search('hd_src:"https', html)
        _qualitysd = re.search('sd_src:"https', html)
        _hd = re.search('hd_src:null', html)
        _sd = re.search('sd_src:null', html)

        lista = []
        _thelist = [_qualityhd, _qualitysd, _hd, _sd]
        for id,val in enumerate(_thelist):
            if val != None:
                lista.append(id)
        main(lista,html)
        return True

    except :
        print("Error")

