print('Welcome to CAROLINA TRIVIA')
print("How well do you know UNC?")
player: str = input("Before you start choose a nickname: ")
student_response: str =input('Are you ready to defend Carolina? yes or no : ')
points: int = 0
total_number_of_questions: int = 5
love_emoji: str  = '\U0001F60D'
sad_emoji: str = '\U0001F613'

def main() -> none:
if student_response == 'yes':
    student_response: int = int(input('Question one:How many carolina Alumni became president of USA?: '))
    if student_response == 2:
        points = points + 1
    print(f'Tar Hell win {love_emoji}')
else:
    print(f'Oh Sorry {sad_emoji}')
    student_response: int = int(input('Question two:Which year was UNC established?: '))
if student_response == 1789:
    points = points + 1
    print(f'Tar Hell win {love_emoji}')
else:
    print(f'Oh sorry {sad_emoji}')
        
student_response: str  = input('Question three: The design of the Old Well was modeled after a similar structure in what country?: ')
if student_response == "France":
   points = points + 1
    print(f'Tar Hell win {love_emoji}')
else:
    print(f'Oh sorry {sad_emoji}')
        
student_response: str = input("Question four: Who was the first student to attend UNC?  ")
if student_response == "Hinton James":
    points = points + 1
    print(f'Tar Hell win {love_emoji}')
else:
    print(f'Oh sorry {sad_emoji}')  
         
student_response:str = input("Question five:Which of UNC’s varsity athletic programs has the most NCAA championship wins?: ")
if student_response == "Women’s soccer":
    points = points + 1
    print(f'Tar Hell win {love_emoji}')
else:
     print(f'Oh sorry{sad_emoji}')  
   
        
print('Thank you for Playing this small quiz game, you attempted',points,"questions correctly!")
mark = (points/total_number_of_questions)*100
print(f'Marks obtained:,{mark}')
if mark <= 50:
    print(f'You scored {mark} and you need to boost your Tar Heel Spirit')
else:
    if mark <= 80:
        print(f'Your tar Heel streek was great today, you scored {mark} Carolina is proud of you')
    else:
        print(f'Youy are a true Tar Heel and Carolina is proud of you, Go Heels!!!')

print(f'Thank you for playing this game {player}')

