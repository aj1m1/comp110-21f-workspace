"""Repeating a beat in a loop."""

__author__ = "730410140"


beat: str = (input("What beat do you want to repeat? "))

Number_of_times: int  = int(input("How many times do you want to repeat it?: "))
if Number_of_times <= 0:
    print("No beat...")
bet: str = ""
while Number_of_times > 0:
    bet = bet + " " + beat
    Number_of_times = Number_of_times - 1
print(bet)

        

            
        

    
  
    



   

 