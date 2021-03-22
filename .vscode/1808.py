n = str(input())
nine = 99

for i in range(0, len(n)):
    while nine != 0:
        if(n[i] == 'H'):
            print("Hello, World!", end=" ")
        elif(n[i] == 'Q'):
            print(n, end = " ")
        elif(n[i] == '9'):
            print(str(nine)+" bottles of beer on the wall," + str(nine) + "bottles of beer.")
            print("Take one down and pass it around, "+ str(nine-1)+ " bottles of beer on the wall.")
            if(nine<0):
                print("No more bottles of beer on the wall, no more bottles of beer.")
                print("Go to the store and buy some more, 99 bottles of beer on the wall.")
        nine -= 1