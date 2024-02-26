import random

def choose_options():
    options = ('rock','paper','scissors')
    user_option = input('Select option: ¿rock, paper or scissors?\n')
    user_option = user_option.lower()
    
    if not user_option in options:
        print('Error: Opción no valida')
        #continue
        return None,None
    computer_option = random.choice(options)
    print('User option =>',user_option)
    print('Computer option =>',computer_option)
    return user_option, computer_option

def check_rules(user_option,computer_option,user_wins,computer_wins):
    if user_option == computer_option:
        print('Draw!')
    elif user_option == 'rock':
        if computer_option == 'scissors':
            print('rock beats scissors')
            print('User win!')
            user_wins += 1
        else:
            print('paper beats rock')
            print('Computer win!')
            computer_wins += 1
    elif user_option == 'paper':
        if computer_option == 'rock':
            print('paper beats rock')
            print('User win!')
            user_wins += 1
        else:
            print('scissors beats paper')
            print('Computer win!')
            computer_wins += 1
    elif user_option == 'scissors':
        if computer_option == 'paper':
            print('scissors beats paper')
            print('User win!')
            user_wins += 1
        else:
            print('rock beats scissors')
            print('Computer win!')
            computer_wins += 1
    return user_wins,computer_wins

def run_game():
    computer_wins=0
    user_wins=0
    rounds=1
    while True:
        print('*'*10)
        print('ROUND #',rounds)
        print('computer_wins',computer_wins)
        print('user_wins',user_wins)
        print('*'*10)
        rounds +=1
        user_option,computer_option=choose_options()
        user_wins,computer_wins=check_rules(user_option,computer_option,user_wins,computer_wins)
        if computer_wins == 2:
            print ('The winner is the computer')
            break
        if user_wins == 2:
            print ('The winner is the user')
            break

run_game()