import random

def high_score():
    try:

        with open("highestscore.txt", "r") as file:
                return int(file.read())
    except:
        return 0

def save_high_score(score):
    file = open ("highestscore.txt","w")
    file.write(str(score))
    file.close()
    
def play_game(num_range,max_attempts):
    random_num = random.randint(1,num_range)
    guess = int(input("Enter your guess: "))
    attempts=0
    
    while attempts < max_attempts:
    
        if guess>random_num:
            print("Too High")
            guess = int(input("Enter your guess: "))
            
        elif guess<random_num:
            print("Too Low")
            guess = int(input("Enter your guess: "))
            
        attempts += 1
        
        if guess == random_num:
            print("Correct!")
            print("Attempts tried:" , attempts)
            score = (max_attempts - attempts + 1) * 10
            return score
    
    print("Attempts are over")
    print("Correct number is: ", random_num)
    return 0
    
def play_again():
    again = input("Do you want to play again ( y / n ): ")
    if again=="y":
        main()
    elif again == "n":
        return
    else:
        print("Invalid answer")

def main():
    highest_score= high_score()
   
    print ("Welcome To The Number Guessing Game!")
    print("Highest score: ", highest_score)   
    print ("1- Easy")
    print ("2- Medium")
    print ("3- Hard")

    level = input("Enter the number of the level: ")
    if level=="1":
        num_range = 20
        max_attempts = 10
             
    elif level=="2":
        num_range = 50
        max_attempts = 8
              
    elif level=="3":
        num_range = 100
        max_attempts = 5
        
    else:
        print("Invalid choice")
        return
        
    score = play_game(num_range,max_attempts)
    print("Your Score:", score)
        
    if score > highest_score:
        print("Congraulations! New High Score!")
        save_high_score(score)
    else:
        print("Try again!")
        
    play_again()
        
if __name__ == "__main__":
    main()

        




