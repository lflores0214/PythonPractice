from googletrans import Translator
translator = Translator()
try:
    with open("test.txt", mode="r") as my_file:
        translated_text = translator.translate(my_file.read(), dest="ja")        
        with open('./test-ja.txt', mode='w') as ja_file:
            ja_file.write(translated_text.text)
except FileNotFoundError as error:
    print("File does not exist. ", error)