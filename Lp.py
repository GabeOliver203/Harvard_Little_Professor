from random import randint

def main():
    print('Welcome to Little Professor!')
    level = Get_Level()
    simulate_round(level)

# Prompts the user for a level. If the user does not input 1, 2, or 3, the program should prompt again. LOOP
def Get_Level():
    while True:
        try:
            level = int(input('Choose a level for your game (1, 2, or 3): '))
            if 1 <= level <= 5:
                break
            else:
                print('Invalid')
        except ValueError:
            print('Invalid')
    return level

def generate_integer(level):
    if level == 1:
        x = randint(0, 9)
        y = randint(0, 9)
    elif level == 2:
        x = randint(10, 29)
        y = randint(10, 29)
    elif level == 3:
        x = randint(30, 59)
        y = randint(30, 59)
    elif level == 4:
        x = randint(60, 99)
        y = randint(60, 99)
    else:
        x = randint(100, 999)
        y = randint(100, 999)
    return x, y

def simulate_round(level):
    correct_answers = 0
    total_rounds = 10
    wrong_answer = 0
    
    for _ in range(total_rounds):
        x, y = generate_integer(level)  # Gere novos números para cada rodada
        cnt_tries = 1 
        while cnt_tries <= 3:
            try:
                answer = int(input(f'{x} + {y} = '))
                if answer == (x + y):
                    correct_answers += 1
                    wrong_answer = 0
                    break
                else:
                    cnt_tries += 1
                    wrong_answer += 1
                    print('EEE')
            except ValueError:
                cnt_tries += 1
                wrong_answer += 1
                print('EEE')
        
        if wrong_answer == 3:
            print(f'{x} + {y} = {x + y}')
            wrong_answer = 0
    
    print(f'score {correct_answers} out of {total_rounds} correct!')

if __name__ == "__main__":
    main()
