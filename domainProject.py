#Get email of user
nameAndEmail = input("What is your email? ")
#Slice Name from the input email
nameOnly = nameAndEmail.split('@',2)
# Print the info of the user
print("Your name is : ", nameOnly[0])
