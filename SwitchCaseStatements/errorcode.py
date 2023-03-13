code = input ("Enter Error Code: ")

match int(code):
    case 100:
        print ("Continue")
    case 200:
        print ("Accepted")
    case 400 | 401:
        print ("Bad Request & Unautorized")
    case _:
        print ("Error code not recognized")