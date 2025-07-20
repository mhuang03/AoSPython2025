def secret_agent_number_generator():
    for i in range(7, 1001, 7):
        print(str(i).rjust(3, "0"))


secret_agent_number_generator()