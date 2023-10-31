def zen():
    # Example of Zen Mode functionality
    print("Zen Mode is active.")
    print("You are in a state of tranquility.")
    print("Press 'Z' to exit Zen Mode.")

    # Here, you can include any Zen Mode actions or functionality you want
    while True:
        user_input = input()
        if user_input.lower() == 'z':
            break

    print("Exiting Zen Mode. Welcome back to the real world.")
