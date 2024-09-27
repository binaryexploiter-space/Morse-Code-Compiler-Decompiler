print("Morse Codes of Army")
def options():
    dict={
        "a":".-",
        "b":"-...",
        "c":"-.-.",
        "d":"-..",
        "e":".",
        "f":"..-.",
        "g":"--.",
        "h":"....",
        "i":"..",
        "j":".---",
        "k":"-.-",
        "l":".-..",
        "m":"--",
        "n":"-.",
        "o":"---",
        "p":".--.",
        "q":"--.-",
        "r":".-.",
        "s":"...",
        "t":"-",
        "u":"..-",
        "v":"...-",
        "w":".--",
        "x":"-..-",
        "y":"-.--",
        "z":"--..",
        " ":"/",
        ".":".-.-.-.",
        ",":"--..--",
        "?":"..--..",
        "!":"-.-.--.",
        "&":".-...",
        "\\":"-..-.",
        ":":"---...",
        ";":"-.-.-.",
        "'":".----.",
        '"':".-..-.",
        "0":"-----",
        "1":".----",
        "2":"..---",
        "3":"...--",
        "4":"....-",
        "5":".....",
        "6":"-....",
        "7":"--...",
        "8":"---..",
        "9":"----.",
        "+":".-.-.",
        "-":"-...-",
        "*":"-.--.-",
        "/":"-..-.",
        "=":"-...-",
        "<":".--.-",
        ">":".-.-",
        "(":"-.--.--.",
        ")":"-.--.--"
    }
    dict2={
        ".-":"a",
        "-...":"b",
        "-.-.":"c",
        "-..":"d",
        ".":"e",
        "..-.":"f",
        "--.":"g",
        "....":"h",
        "..":"i",
        ".---":"j",
        "-.-":"k",
        ".-..":"l",
        "--":"m",
        "-.":"n",
        "---":"o",
        ".--.":"p",
        "--.-":"q",
        ".-.":"r",
        "...":"s",
        "-":"t",
        "..-":"u",
        "...-":"v",
        ".--":"w",
        "-..-":"x",
        "-.--":"y",
        "--..":"z",
        "/":" ",
        ".-.-.-.":".",
        "--..--":",",
        "..--..":"?",
        "-.-.--.":"!",
        ".-...":"&",
        "-..-.":"/",
        "---...":":",
        "-.-.-.":";",
        "'":".----.",
        ".-..-.":'"',
        "-----":"0",
        ".----":"1",
        "..---":"2",
        "...--":"3",
        "....-":"4",
        ".....":"5",
        "-....":"6",
        "--...":"7",
        "---..":"8",
        "----.":"9",
        ".-.-.":"+",
        "-...-":["-","="],
        "-.--.-":"*",
        ".--.-":"<",
        ".-.-":">",
        "-.--.--.":"(",
        "-.--.--":")"
    }
    list=[]
    secondList=[]
    thirdList=[]
    print("Options")
    print("")
    print("1. Morse Code Compiler")
    print("2. Morse Code Reader")
    print("3. About Morse Codes")
    print("4. Online Translators")
    print("5. Contact US")
    print("")
    option=int(input("> "))
    if(option == 1):
        print("")
        print("Morse Code Compiler")
        print("")
        firstText=input("Enter text: ")
        print("Your text: "+firstText)
        text=firstText.lower()
        splitedText=text.split()
        lengthText=len(splitedText)
        lastIndex=lengthText-1
        for letter in text:
            list.append(letter)
        for i in list:
            secondList.append(dict[i]+" ")
        listToStr = ''.join([str(elem) for elem in secondList])
        print("Morse code: "+listToStr)
        print("____________________________________________________________")
        print("")
    elif(option==2):
        print("")
        print("Morse Code Reader")
        print("")
        text = input("Enter text: ")
        print("Morse code: " + text)
        splitedText = text.split()
        lengthText = len(splitedText)
        lastIndex = lengthText - 1
        for i in splitedText:
            thirdList.append(dict2[i])
        listToStr = ''.join([str(elem) for elem in thirdList])
        print("Decoded text: " + listToStr)
        print("____________________________________________________________")
        print("")
    elif(option==3):
        print("")
        print("____________________________________________________________")
        print("""Morse code is a method used in telecommunication to encode text characters as standardized sequences of two different signal durations, called dots and dashes, or dits and dahs. Morse code is named after Samuel Morse, one of the inventors of the telegraph.""")
        print("____________________________________________________________")
        print("")
    elif(option==4):
        print("")
        print("____________________________________________________________")
        print("Morse codes online translators")
        print("")
        print("https://morsecode.world/international/translator.html")
        print("https://morsedecoder.com/")
        print("https://capitalizemytitle.com/morse-code-translator/")
        print("https://www.morsecode-translator.com/")
        print("http://www.unit-conversion.info/texttools/morse-code/")
        print("https://scoutlife.org/hobbies-projects/funstuff/575/morse-code-translator/")
        print("https://www.boxentriq.com/code-breaking/morse-code")
        print("https://www.lexilogos.com/keyboard/morse.htm")
        print("https://academo.org/demos/morse-code-translator/")
        print("https://blog.aspose.com/font/morse-code-translator/")
        print("____________________________________________________________")
        print("")
    elif(option==5):
        print("")
        print("____________________________________________________________")
        print("Contact Info")
        print("")
        print("Name: Web Designs Codes LK")
        print("Telegram: @dom_black_hat")
        print("Whatsapp: +94 71 101 9707")
        print("____________________________________________________________")
        print("")
while(True):
    options()
