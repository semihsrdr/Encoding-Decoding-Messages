
import time
alfabe = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(message,shift):
    encoded_message=[]
    for letter in message:
        for position in range(len(alfabe)):
            if alfabe[position]==letter:
                if position+shift>26:
                    encoded_message.append(alfabe[position+shift-27])
                else:
                    encoded_message.append(alfabe[position+shift])
    print("Your message is encoding. Please Wait...")
    time.sleep(0.5)
    print("Encoded message : ",end="")
    for i in encoded_message:
        print(i,end="")
    print()
    print()


def decode(message,shift):
    decoded_message=[]
    for letter in message:
        for position in range(len(alfabe)):
            if alfabe[position]==letter:
                if position-shift<0:
                    decoded_message.append(alfabe[27-(shift-position)])
                else:
                    decoded_message.append(alfabe[position-shift])
                    #4 verdik diyelim 4-9 yapınca 9-4 yapıp daha sonra 26-(9-4) yapmak gerek
    print("Your message is encoding. Please Wait...")
    time.sleep(0.5)
    print("Decoded message : ", end="")
    for i in decoded_message:
        print(i, end="")
    print()
    print()

while True:
    chose=input("Do you wanna encode or decode : ")
    if chose.lower()=="encode":
        message=input("Write your message for encoding: ")
        shift=int(input("Enter the shift : "))
        encode(message,shift)
        stop=input("if you wanna finish please write finish : ")
        if stop=="finish":
            print("Program is shutting down")
            break


    elif chose.lower()=="decode":
        message=input("Write your message for decoding : ")
        shift=int(input("Enter the shift : "))
        decode(message,shift)
        stop = input("if you wanna finish please write finish : ")
        if stop == "finish":
            print("Program is shutting down")
            break
    else:
        print("Please write ' encode or decode! '")