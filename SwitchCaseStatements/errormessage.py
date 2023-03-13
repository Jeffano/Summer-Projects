message = "65"

if message.isdigit():
    response = {"data": message}
else:
    response = {"error": message}

match response:
    case {"error": msg}:
        print ("Error: ",msg)
    case {"data": data}:
        print ("Recieved Data: ", data)