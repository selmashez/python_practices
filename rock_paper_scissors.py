import random
import colorama
from colorama import Fore

choises=['r' , 'p' , 's']
meaning_of_choises={
    'r':'rock',
    's':'scissors',
    'p':'paper'
}
user_score=0
ai_score=0

while True:
    user_choise=input(Fore.LIGHTBLACK_EX + "enter your choise: ")
    ai_choise=random.choice(choises)
    if user_choise in choises:
        print(Fore.BLUE+f'your choise is {meaning_of_choises[user_choise]} and ai choise is {meaning_of_choises[ai_choise]}')
        if user_choise==ai_choise:
            print(Fore.YELLOW+"tie" )
            continue
        elif (user_choise=='r' and ai_choise=='s') or (user_choise=='s' and ai_choise=='p') or (user_choise=='p' and ai_choise=='r'):
            user_score=user_score+1
            if user_score==3:
                print(Fore.GREEN+"you won" , '\U0001F603')
                break
            
        else:
            ai_score=ai_score+1
            if ai_score==3:
                print(Fore.RED+"you lost" , '\U0001F625')
                break
    else:
        print(Fore.MAGENTA+"invalied input!!!",'\U0001F62A')
        break
