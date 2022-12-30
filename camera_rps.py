
import cv2
from keras.models import load_model
from time import time 
import numpy as np
import random 

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def get_prediction():
    player_choice = None
    max_time = 7 
    start = time()

    while (time() - start)<max_time: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        player_choice = np.argmax(prediction,axis=-1)   
        if cv2.waitKey(1) & 0xFF == ord('q'):
           break
            
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    return player_choice[0]


def get_computer_choice():
    options = ["Rock","Paper","Scissors"]
    chose = random.choice(options)
    return chose 

def get_winner(computer_choice,user_choice):
    if (computer_choice == "Paper" and user_choice == 2) or (computer_choice == "Rock" and user_choice == 0) or (computer_choice == "Scissors" and user_choice == 1) :
        return("It is a tie!")
    elif (computer_choice == "Paper" and user_choice == 1) or (computer_choice == "Rock" and user_choice == 2) or (computer_choice == "Scissors" and user_choice == 0): 
        return("You won")
    else:
        return("You lost")                       

def play():
    pwin = 0 
    cwin = 0 
    for i in range(3):
      playa = get_prediction()
      comp = get_computer_choice()
      print("Player: {} Comp: {}".format(playa, comp))
      res  = get_winner(comp,playa)
      if res == "You won":
        pwin = pwin + 1
      elif res == "You lost":
        cwin = cwin + 1  

    if pwin > cwin:
        print("Player won the game!")
    elif pwin < cwin:
        print("You lost the game!")  
    else:
        print("It is a tie!")          
    

    








