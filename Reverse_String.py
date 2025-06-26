def reverse(text:str):
    
    new_text = "".join(reversed(list(text)))
    print(new_text)
    return new_text

reverse("robot")