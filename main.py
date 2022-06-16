import time
chars = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
charlist = chars.replace("", "|").split("|")
overboard = False
restart = "y"

while restart == "y":
    key = int(input("What is your key? A NUMBER \n"))
    Option =input(
    "Would you like to encrypt (make secret message) or decrypt (solve secret message)? (Use either E or D or this wont work.) \n")
    option = Option.casefold()

    if key >= 63:
        key = key%63
        overboard = True
    if option == "e":
        text = input("What is your message? \n")
        textplus = text + "|"
        length = textplus.index("|")
        textlist = text.replace("", "|").split("|")
        counter = 0
        encMes = ""

        while counter <= length:
            charLetter = chars.index(textlist[counter])
            encrypt = charLetter + key
            encChar = charlist[encrypt + 1]
            encMes = encMes + encChar
            counter += 1

        print(encMes)

        time.sleep(5)
        Restart = input("Would you like to restart? (Only use y or n) \n")
        restart = Restart.casefold()

    if option == "d":
        encMes = input("What is the message you want to decrypt? \n")

        # If you want to copy something remove the "input" and the parentheses and put your message inside of the quotation points.

        meslist = encMes.replace("", "|").split("|")
        deMes = ""
        counter2 = 2
        encplus = encMes + "|"
        lengthm = encplus.index("|")

        while counter2 <= lengthm:
            charLetter = chars.index(meslist[counter2])
            if overboard == True:
                charLetter = charLetter + 63

            decrypt = charLetter - key
            deChar = charlist[decrypt + 1]
            deMes = deMes + deChar
            counter2 += 1

        print(deMes)

        time.sleep(5)

        Restart = input("Would you like to restart? (Only use y or n) \n")
        restart = Restart.casefold()