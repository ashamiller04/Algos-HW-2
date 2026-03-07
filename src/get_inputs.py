def get_input(filename):
    requests = []

    with open(f"../data/{filename}", 'r') as file:
        #Whole file
        everything = file.read()

        everything = everything.split()

        # reading capacity and number of requests
        k = int(everything[0])
        m = int(everything[1])
        everything.pop(0)
        everything.pop(0)

        # reading IDs
        requests = everything

    return k, m, requests

#also seems to be working