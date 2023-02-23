import operator
import random

player_name= input ('Please enter your name: ')
print  ('Welcome ' + player_name)
print ('Rules of this game:')
print ('1. You will answer 10 question about addition of two number')
print ('2. Each time your guess is correct, you will get 9 points')
print ('3. If your answer is incorrect, you will get lose 10 points')
print("4. the game will be over if your points are below 0")
print ('Good luck!')



total_score=0

for attempt in [1,2,3,4,5,6,7,8,9,10]:
   num_A = random.randint (1,9)
   num_B = random.randint (0,10)

   answer = input ('What is addition of '+str(num_A)+' and '+str(num_B)+': ')
   if int (answer) == num_A + num_B:
      total_score = total_score + 9
      print ('Correct! your total points are ' + str(total_score))
   elif int (answer) != num_A + num_B:
      total_score = total_score - 10

      print ('Wrong! your total points are ' + str(total_score))

   if total_score < 0:
      print('Sorry your point is below 0. You lost!')
      break
   print('Your score is ' + str(total_score))


