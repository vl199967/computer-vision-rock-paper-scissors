# Computer Vision RPS
# Milestone 2 
- trained and exported the model and put it into the main project folder 
- The model was trained using 4 classes of images of hand gesturing rock paper scissor and nothing. 
- Each class have equal representation, which means each class have roughly the same amount of training sample images. 
- If a model is trained on a dataset with severe class imbalance, it is very likely that the prediction the model makes 
- is trivial and simply reflects underlying class distribution.
- to make the model more robust I varied the way the hand gestures were represented in the dataset. Sometimes the gestures were against a pure-coloured background like a white wall, or against a complex background with other visual distractions like furnitures. This is to make sure the model learns from the right representation and becomes noise-tolerant. 
- Initially the model struggled to make the distinction between paper and scissor, but the problem was solved with more training images involved. 
- after training and validation I exported the model as a h5 file and stored it in my project folder.

# Milestone 4 
- Initially I did not have tensorflow installed in my virtual environment, rendering the manual_rps file unusable. I had to create a new virtual environment, install the tensorflow version specifically made for M1 macs and all its dependencies, re-install all previous dependencies, scrap the previous requirement.txt , make a new one and clone the enviroment. The logic of the game was encapsulated with a typical if-elif-else statement. If both parties did not reach a tie, we check all the scenarios where the user wins. All the remaining cases (e.g player chooses scissor and computer chooses paper) result in the player losing, so we do not have to enumerate through them one by one.
