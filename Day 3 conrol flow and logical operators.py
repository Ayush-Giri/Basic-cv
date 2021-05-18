user_order = input("what size pizza would you like small is for $15 medium is for $20 and large is for $25 ")
if user_order == "small":
    small_pepperoni = input("would you like small pepporini for $2 ")
    extra_cheese = input("would you like extra cheese for $1 ")
    if small_pepperoni == "yes" and extra_cheese == "yes":
        print(f"your total becomes ${15 + 2 + 1}")
    elif small_pepperoni == "yes" and extra_cheese == "no":
        print(f"your total becomes ${15 + 2}")
    elif small_pepperoni == "no" and extra_cheese == "yes":
        print(f"your total becomes ${15 + 1}")
    elif small_pepperoni == "no" and extra_cheese == "no":
        print("your total becomes $15")


elif user_order == "medium":
    medium_pepperoni = input("would you like pepperoni ")
    extra_cheese = input("would you like extra cheese ")
    if medium_pepperoni == "yes" and extra_cheese == "yes":
        print(f"your total becomes ${20 + 3 + 1}")
    elif medium_pepperoni == "yes" and extra_cheese == "no":
        print(f"your total becomes ${20 + 3}")
    elif medium_pepperoni == "no" and extra_cheese == "yes":
        print(f"your total becomes ${20 + 1}")
    elif medium_pepperoni == "no" and extra_cheese == "no":
        print("your total becomes $20")



elif user_order == "large":
    large_pepperoni = input("would you like extra peppperoni ")
    extra_cheese = input("would you like extra_cheese ")
    if large_pepperoni == "yes" and extra_cheese == "yes":
        print(f"your total becomes ${25 + 1 + 3}")
    elif large_pepperoni == "yes" and extra_cheese == "no":
        print(f"your total becomes ${25 + 3}")
    elif large_pepperoni == "no" and extra_cheese == "yes":
        print(f"your total becomes ${25 + 1}")
    elif large_pepperoni == "no" and extra_cheese == "no":
        print("your total becomes $25")


else:
    print("please restart the program and enter a valid input")