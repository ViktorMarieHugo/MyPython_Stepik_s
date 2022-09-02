def is_valid():
    while True:
        n = input("Enter digit from 1 to 100 \n")
        if n.isdigit():
            if 1<=int(n)<=100:
                return int(n)
            else:
                print("Enter ONLY digits! FROM 1 to 100 !")
        else:
            print("Enter only digits! Try again.")