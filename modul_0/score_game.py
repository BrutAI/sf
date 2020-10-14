import numpy as np

def game_core_v3(number):
    '''Каждый раз закадываем число в центе, при этом запоминаем границы и уменьшаем поле на котором играем'''
    count = 1
    predict = 50 # Начинаем с середины
    left_wall = 0 # Наша стена Слева
    right_wall = 101 # Наша стена Справа
    
    while number != predict: 
        count+=1
        if number > predict:
            left_wall = predict
            predict = int((right_wall-predict)/2)+predict
        elif number < predict:
            right_wall = predict
            predict = int((predict-left_wall)/2)
    return(count) # выход из цикла, если угадали 
        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v3)