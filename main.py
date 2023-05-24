from moduls import *
user_data = input("Enter your data: ")
user_operation = input("Enter your considerd operation: ")
user_shuffle_time = int(input("Enter your loop number for shuffle:"))

#shuffle
for i in range(user_shuffle_time):
    shuffled = "".join(random.sample(alphas, len(alphas)))
#write to file
my_file = open("file.txt", "r+")
my_file.write(user_data)
print(alphas)
print(shuffled)
print(user_data)
encrypted = encryption2(user_data ,shuffled)
print(encrypted)
my_file.write(encrypted)
#print(encryped)
#decrypt
user_check = input("Enter value that you want to check: ")
if user_operation.lower() == "d":
    decrypted = decryption2(user_check, shuffle=shuffled)
    #print("hi")
    print(decrypted)

my_file.close()