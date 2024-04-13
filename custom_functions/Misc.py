import uuid



def loginCheck(email,password):
    #nothing happens

    return True



def getUserInfo(email,password):
    
    if email == "mikk655i@stud.kea.dk":
        id = "1"
        type = "artist"
    else:
        id = uuid.uuid4()
        type = "user"

    results = {"type": type, "id": id}
    return results


