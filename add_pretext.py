import os


replace = False
""" True means remove the code inserted. On first run it does nothing, on second run, it removes the code from file 
name. Change to False if you have run the script once and do not want to remove. Use if error exists and correction
 is needed."""


dict_items = {
    "ENE": ("Energy", "30"),
    "MAT": ("Materials", "07"),
    "MAN": ("Management", "0"),
    "HEA": ("HealthAndWellbeing", "11"),
    "TRA": ("Transport", "04"),
    "WAT": ("Water", "10"),
    "LE": ("Ecology", "02"),
    "POL": ("Pollution", "06"),
    "WST": ("Waste", "02")
}


def find_criteria(criteria):
    # gets the folder name and splits into a list to get the credit
    new_word = criteria.split("_")
    return new_word[0]


def find_number_of_criteria(criteria):
    # gets the credit from find_criteria and picks out the last two letters
    credit_number = criteria[-2:]
    return credit_number


def create_title(criteria):
    # cauta in dictionar daca cheile sunt in numele creditului si apoi atribuie in functie de "if" un nume luat din
    # valorile din dictionar
    for i in dict_items.keys():
        if i in find_criteria(criteria):
            if find_number_of_criteria(find_criteria(criteria)) <= dict_items[i][1]:
                title = "Part1" + "_" + dict_items[i][0]
            else:
                title = "Part2" + "_" + dict_items[i][0]
    return title


def add_pretext(new_path, project_code):
    new_path_1 = ""

    lista = list(new_path)
    for i in range(len(lista)):
        if lista[i] == "\\":
            lista[i] = "/"
        new_path_1 += lista[i]
    new_path_1 += "/"

    lista_foldere = os.listdir(path=new_path_1)
    for i in range(len(lista_foldere)):
        # cauta in lista de foldere pentru a afla numele de credit
        lista_fisiere = os.listdir(path=new_path_1 + lista_foldere[i])
        credit = lista_foldere[i]
        # creeare de cod de inserat in file name
        front_part_text = project_code + "_" + create_title(credit) + "_" + find_criteria(
            credit)

        # citire fiecare fisier, verificare daca e sau nu formatul cerut, redenumire
        for j in range(len(lista_fisiere)):
            if front_part_text not in lista_fisiere[j]:
                if lista_fisiere[j].endswith(".pdf") or lista_fisiere[j].endswith(".PDF")  \
                        or lista_fisiere[j].endswith(".xlsx") or lista_fisiere[j].endswith(".XLSX") \
                        or lista_fisiere[j].endswith(".xlsm") or lista_fisiere[j].endswith(".XLSM") \
                        or lista_fisiere[j].endswith(".jpeg") or lista_fisiere[j].endswith(".JPEG")\
                        or lista_fisiere[j].endswith(".jpg") or lista_fisiere[j].endswith(".JPG")\
                        or lista_fisiere[j].endswith(".png") or lista_fisiere[j].endswith(".PNG") \
                        or lista_fisiere[j].endswith(".doc") or lista_fisiere[j].endswith(".DOC") \
                        or lista_fisiere[j].endswith(".docx") or lista_fisiere[j].endswith(".DOCX") \
                        or lista_fisiere[j].endswith(".msg") or lista_fisiere[j].endswith(".MSG") \
                        or lista_fisiere[j].endswith(".csv") or lista_fisiere[j].endswith(".CSV"):
                    new_file_name = front_part_text + "_" + lista_fisiere[j]
                    file_name_path = new_path_1 + lista_foldere[i] + "/" + lista_fisiere[j]
                    new_file_name_path = new_path_1 + lista_foldere[i] + "/" + new_file_name
                    if len(new_file_name_path)<256:
                        os.rename(file_name_path,new_file_name_path)
                    else:
                        print(new_file_name_path)
                    f = open("fisiere.txt", "a", encoding='utf8')
                    f.write('{}\n'.format(new_file_name_path))
                    f.close()
            if front_part_text in lista_fisiere[j] and replace is True:
                short_file_name = lista_fisiere[j].replace(front_part_text+"_", "")
                file_name_path = new_path_1 + lista_foldere[i] + "/" + lista_fisiere[j]
                short_file_name_path = new_path_1 + lista_foldere[i] + "/" + short_file_name
                os.rename(file_name_path, short_file_name_path)

    print("finish run")