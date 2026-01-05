#Get email of user
nameAndEmail = input("What is your email? ")
#Slice Name from the input email
nameAndDomainSplit = nameAndEmail.split('@',2)
# Print the info of the user
print("Your name is : ", nameAndDomainSplit[0])
# Print the domain of the email
print("Your domain is: ", nameAndDomainSplit[1])
