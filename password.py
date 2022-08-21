pws = open("passwords.txt", "a")
pws.write(' \n \n')
password = input("Enter your password: ").upper().lower()
confirm = ''
while confirm != password:
   confirm = input("Confirm Your Password: ").upper().lower()
print("Success!!!")

pws.write("Password  =  " + password +'\n' + 'Confirmed Password  = '+ password)
 # Login Section
pass_word = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False
while pass_word != password and not out_of_guesses:
   if guess_count < guess_limit:
      pass_word = input("Enter Your PASSWORD !!!: ")
      guess_count += 1
   else:
      out_of_guesses = True
if out_of_guesses:
   print("YOU ENTERED TO MANY INCORRECT PASSWORDS. \n Refresh The Program And Try Again !!! ")
else:
   print("You Have Successfully Logged In !! \n ENJOY YOUR TOUR  ")




