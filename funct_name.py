def hi(lang, name):
    if lang == "en":
        print("HELLO!", name + ",", "how are you?")

    elif lang == "ru":
        print("Привет!", name + ",", "как дела?")
    elif lang == 'ro':
        print("Salut!", name + ",", "ce mai faci?")
    else:
        print(f'ERROR {lang} is not recognized!!!') 

lang = input("ENTER language (en, ru, ro)- ")
name = input("ENTER NAME- ")
hi(lang, name)