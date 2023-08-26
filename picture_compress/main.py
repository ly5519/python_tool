from PIL import Image
import os
import math
from re_use import get_num_and_unit


if __name__ == "__main__":
    img_path = input("input picture path:")
    img = Image.open(img_path)
    suffix = img_path[-3:]
    scale = img.size[0]/img.size[1]
    count_pixel = img.size[0] * img.size[1]

    print(suffix)
    if suffix == "png":
        choose = input("is a png picture, do you want to use jpg?[Y/n]:")

        if choose.upper() in ['Y', "YES"]:
            img = img.convert("RGB")
            suffix = "jpg"
            
    img.save("tmp." + suffix)

    img_size = os.path.getsize("tmp."+suffix)
    unit = ["B", "KB", "MB", "GB", "..."]
    unit_idx = 0
    while (img_size / math.pow(1024, unit_idx)) >= 1024:
        unit_idx += 1

    print("current size：%.2f" % (img_size / math.pow(1024, unit_idx)), unit[unit_idx])

    wanna_size = input("you wanna size: ")
    split_res = get_num_and_unit(wanna_size)
    out_size = split_res[0] * math.pow(1024, unit.index(split_res[1]))

    mp = out_size/img_size

    w = img.size[0]
    h = img.size[1]
    out_w = (mp * count_pixel * scale) ** 0.5
    img = img.resize((int(out_w), int(h * (out_w/img.size[0]))))
    img.save("out."+suffix)





