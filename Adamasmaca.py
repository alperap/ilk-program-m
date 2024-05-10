
print("Hii, lets begin!")

Word = "alperap"

gamer_word=""
    
lives = 10

while lives >0 :
    
    word_gamer_character = 0

    for word in Word:
        if word in gamer_word:
            print(word)
        else:
            print("-")
            word_gamer_character +=1

    if word_gamer_character == 0:
        print("u won!")
        break

    entry = input("Enter any character: ")

    if entry in Word:
        gamer_word += entry
        print("Nice, u find it")
        print(f"Your lives: {lives}")
    elif entry not in Word:
        print("Was wrong :(")
        lives -=1
        print(f"Your lives: {lives}")
    
    




