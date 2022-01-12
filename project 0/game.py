<<<<<<< HEAD
import numpy as np

number = np.random.randint(1,101) #загадываем число

count = 0

while True:
    count+=1
    predict_number=int(input("Угадай число от 1 до 100: "))
    
    if predict_number>number:
        print("Число должно быть меньше")
        
    elif predict_number<number:
        print("Число должно быть больше")
        
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
=======
import numpy as np

number = np.random.randint(1,101) #загадываем число

count = 0

while True:
    count+=1
    predict_number=int(input("Угадай число от 1 до 100: "))
    
    if predict_number>number:
        print("Число должно быть меньше")
        
    elif predict_number<number:
        print("Число должно быть больше")
        
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
>>>>>>> 71b6c311463668bdd8b10e0490cd4e0a1fd4f26a
        break #Конец игры, выход из цикла