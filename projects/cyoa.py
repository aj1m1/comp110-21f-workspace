"""Carolina Trivia game."""

__author__ = "730410140"

points: int
player: str 
love_emoji: str = '\U0001F60D'
sad_emoji: str = '\U0001F613'
count: int
total_number_of_questions: int = 5




def main() -> None:
    """Entry point of game."""
    greet()
    points = 0
    points += run_game(points)         
    play_again = input("Do you want to play again? yes/no: ")
    while play_again == "yes":
        points += run_game(points)
        play_again = input("Do you want to play again? yes/no: ")
    final_score(points)
    print("Goodbye")
    

def greet() -> None:
    """Introduction to game."""
    print("Welcome to Carolina Trivia Game.")
    player = str(input("Before you start this Carolina Trivia , Enter your name: "))
    print(f'Welcome {player}!!!')
    return
        

def game_one(points: int) -> int:
    """Carolina academics history game."""
    student_response1 = (int(input('Question two:Which year was UNC established?: ')))
    if student_response1 == 1789:
        points = points + 1
        print(f'Tar Hell win {love_emoji}')
    else:
        print(f'Oh Sorry {sad_emoji}')

    student_response2: str = input("Who was the first student to attend UNC?  ")
    if student_response2 == "Hinton James":
        points = points + 1
        print(f'Tar Hell win {love_emoji}')
    else:
        print(f'Oh Sorry {sad_emoji}')
    
    student_response3: str = input('Question three: The design of the Old Well was modeled after a similar structure in what country?: ')
    if student_response3 == "France":
        points = points + 1
        print(f'Tar Hell win {love_emoji}')
    else:
        print(f'Oh Sorry {sad_emoji}')

    student_response4: str = input('UNC has 5 buildings named after members of the same family. What is the family? : ')
    if student_response4 == "Kenan":
        points = points + 1
        print(f'Tar Hell win {love_emoji}')
    else:
        print(f'Oh Sorry {sad_emoji}')

    student_response5: int = int(input("How many students were in UNC’s first graduating class?: "))
    if student_response5 == 7:
        points = points + 1
        print(f'Tar Hell win {love_emoji}')
    else:
        print(f'Oh Sorry {sad_emoji}')

    return points


def game_two(points: int) -> int:
    """Carolina sports game."""
    student_responseone: str = (input('What UNC sports team was, for a time, known as the “White Phantoms?: '))
    if student_responseone == "Basketball team":
        points = points + 1
        print(f'Tar Heel win {love_emoji}')
    else:
        print(f'Oh Sorry {sad_emoji}')
  
    student_response_two: str = input("Which of UNC’s varsity athletic programs has the most NCAA championship wins?: ")
    if student_response_two == "Women's soccer":
        points = points + 1
        print(f'Tar Heel win {love_emoji}')
    else:
        print(f'Oh Sorry {sad_emoji}')

    student_response_three = (int(input("When was the last time UNC Basketball win NCAA?: ")))
    if student_response_three == 2017:
        points = points + 1
        print(f'Tar Heel win {love_emoji}')
    else:
        print(f'Oh Sorry {sad_emoji}')

    student_response_four: int = (int(input('How many times has the UNC women soccer won the NCAA?: ')))
    if student_response_four == 23:
        points = points + 1
        print(f'Tar Heel win {love_emoji}')
    else:
        print(f'Oh Sorry {sad_emoji}')
  
    student_response_five: str = (input('What is the last sport UNC won NCAA ?: '))
    if student_response_five == "Men's Tennis":
        points = points + 1
        print(f'Tar Hell win {love_emoji}')
    else:
        print(f'Oh Sorry {sad_emoji}')

    return points


def game_off(points: int) -> int:
    """Get off the game."""
    print(f'Thank you for Playing this game, you attempted" {points}  "questions correctly!')
    mark = (points / total_number_of_questions) * 100
    print(f'Marks obtained: {mark}')
    if mark <= 50:
        print(f'You scored {mark} and you need to boost your Tar Heel Spirit')
    else:
        if mark <= 80:
            print(f'Your tar Heel streek was great today, you scored {mark} Carolina is proud of you')
        else:
            print('Youy are a true Tar Heel and Carolina is proud of you, Go Heels!!!')
    
    return points


def run_game(points: int) -> int:
    """How game runs."""
    count = 0

    while True:
        print('Choose one of the following, UNC SPORTS , UNC ACADEMICS HISTORY, or EXIT')
        student_response = input("Your choice: ")
        if student_response == "UNC ACADEMICS HISTORY":
            points = game_one(points)
            return game_off(points)
        else:
            if student_response == "UNC SPORTS":
                points = game_two(points)
                return game_off(points)
            else:
                student_response = input("Do you want to Exit?, yes or no:")
                if student_response == "yes":
                    
                    count += 1
        return game_off(points)
    

def final_score(points: int) -> float:
    """Scores calculation."""
    total_score = (points / (count * 5)) * 100
    return total_score


if __name__ == "__main__":
    main()
