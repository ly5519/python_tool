from download import get_pdf_picture


target_dir = r'C:\Users\Liu_Yan\Desktop\教案'

curr_name = input("name:")


seed_list = {}

seed = input("input the seed:")
seed = seed[:-8]

seed_list["实施报告研析"] = seed + "YmcucGRm"
seed_list["教案研析"] = seed + "amEucGRm"
seed_list["作品鉴赏"] = seed + "ZHgucGRm"

for key, val in seed_list.items():
    get_pdf_picture(val, f"{target_dir}\\{curr_name}\\{key}\\")
