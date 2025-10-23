import json

def seria_card():
    seria = input("Iltimos karta seriasini kiriting: ")
    with open("bonkamat_meneger.json", "r") as file:
        data = json.load(file)
        for key,item in data.items():
            if item["seria"] == seria:
                return key,item
    return False

def password_card():
    data_card = seria_card()
    if data_card:
        count = 0
        print("\nESLATMA: Karta parolini to'g'ri kiritish uchun sizda >> 3 << ta urinish bor! Aks holda karta bloklanadi!\n")
        while count < 3:
            password = input("Karta parolini kiriting: ")
            if data_card[1]["password"] == password:
                return data_card
            count += 1
            if count < 3:
                print(f"\nParol noto'g'ri! Sizda yana {3 - count} ta urinish qoldi.\n")
        print("\nKarta bloklandi! Iltimos bankka murojaat qiling.\n")
        return None
    else:
        print("\nBunday seria topilmadi! Iltimos programmani qayta ishga tushiring!!!\n")
        return None

def balans_card(data_card:tuple):
    data = data_card[1]
    while True:
        print(f"\nKartadagi balansingiz: {data["balans"]} $")
        kod = input("\n>> 1 <<   Davom ettirish\n>> 2 <<   Tugatish\n")
        if kod == "1":
            return True
        else:
            return False

def update_card(key:int,item:dict):
    with open("../bonkamat_meneger.json", "r") as file:
        data = json.load(file)
        data[f"{key}"] = item
        print(data[f"{key}"])
        with open("../bonkamat_meneger.json", "w") as file1:
            json.dump(data, file1, indent=4)

def pul_yechish(key:int,item:dict):
    max_pul=item["balans"]
    print("\n>> 0 <<  Orqaga qaytish\n")
    pul = float(input("Yechmoqchi bo'lgan summani kiriting $:"))
    while True:
        if max_pul > pul > 0:
            print(f"\nHisobdagi summa: {max_pul} $\nYechiladigan summa: {pul} $\nKamissiya 1%: {pul*0.01} $\nYmumiy yechiladigan summa: {pul+(pul*0.01)} $")
            ruhsat = float(input("\n>> 1 <<   Tastiqlash\n>> 2 <<   Bekor qilish\n"))
            if ruhsat == 1:
                max_pul-=pul+(pul*0.01)
                item["balans"] = max_pul
                update_card(key,item)
                print(f"Hisobingizdan {pul+pul*0.01} $ yechildi")
                print(f"\n\tChek\nF.I.: {item["ower"]}\nKarta raqami: {item["seria"]}\nYechiladigan summa: {pul} $\nKamissiya 1%: {pul * 0.01} $\nUmumiy yechilgan summa: {pul + (pul * 0.01)} $\nHisobdagi summa: {item["balans"]} $\n")
                break
            else:break
        elif pul == 0:break
        else:
            pul = float(input(f"Hisobingizda {pul} $ chiqmaydi. Iltimos yechmoqchi bo'lgan summani qayta kiriting:"))

def pul_qushish(key:int,item:dict):
    max_pul=item["balans"]
    print("\n>> 0 <<  Orqaga qaytish\n")
    pul = float(input("Qo'shmoqchi bo'lgan summani kiriting $:"))
    while True:
        if pul > 0:
            print(f"\nHisobdagi summa: {max_pul} $\nQo'shiladigan summa: {pul} $\nKamissiya 1%: {pul * 0.01} $\nYmumiy qo'shiladigan summa: {pul - (pul * 0.01)} $")
            ruhsat = float(input("\n>> 1 <<   Tastiqlash\n>> 2 <<   Bekor qilish\n"))
            if ruhsat == 1:
                max_pul+=pul-(pul*0.01)
                item["balans"] = max_pul
                update_card(key,item)
                print(f"Hisobingizga {pul-(pul*0.01)} $ qo'shildi")
                print(f"\n\tChek\nF.I.: {item["ower"]}\nKarta raqami: {item["seria"]}\nQo'shiladigan summa: {pul} $\nKamissiya 1%: {pul * 0.01} $\nUmumiy qo'shilgan summa: {pul - (pul * 0.01)} $\nHisobdagi summa: {item["balans"]} $\n")
                break
            else:break
        elif pul == 0:break
        else:
            pul = float(input(f" {pul} $ - bunday summa mavjud emas. Iltimos qo'shmoqchi bo'lgan summani qayta kiriting:"))


def meneger_card():
    print("\n\tBonkamatga hush kelibsiz!\n")
    data_card = password_card()
    if not data_card:
        return
    while True:
        kod = input("\n>> 1 <<   Balansni ko'rish\n>> 2 <<   Pul yechish\n>> 3 <<   Pul qo'shish\n>> 4 <<   Tugatish\n")
        if kod == "1":
            if balans_card(data_card):
                continue
            else:
                break
        elif kod == "2":
            pul_yechish(data_card[0], data_card[1])
        elif kod == "3":
            pul_qushish(data_card[0], data_card[1])
        else:
            break

meneger_card()

