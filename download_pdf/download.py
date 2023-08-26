import os.path
import requests
import json
from pic_to_pdf import pic2pdf2

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}


def get_pdf_picture(pdf_address: str, save_file: str):

    if not os.path.exists(save_file):
        os.makedirs(save_file)

    idx = 0

    while True:
        response = requests.get(url=f"https://doctrans.36ve.com/PW/GetPage?f={pdf_address}&img=&isMobile=false&readLimit=&sn={idx}&furl=", headers=header)
        tmp = json.loads(response.text)

        img_address = tmp['NextPage']

        if img_address == 'Over':
            break

        download_stream(f"https://doctrans.36ve.com/img?img={img_address}&tp=", f"{save_file}{idx}.png")

        print(f"{tmp['PageIndex']}/{tmp['PageCount']}")

        idx += 1

    pic2pdf2(f"{save_file}*")
    print(f"{save_file} completed!!!")


def download_stream(url: str, save_address: str):
    r = requests.get(url=url, stream=True)
    with open(save_address, 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)



