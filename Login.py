DB = {

}

def register(name, email, password):
    if not email.endswith("@gmail.com"):
        return "Invalid email"
    
    if not len(password) >= 8:
            return "Password must be 8 characters long"
    
    if email in DB:
        return "Email already exists"
    
    DB[email] = {"name":name, "password":password}
    return "Registeration successfull"


def login(email, password):
    if email not in DB:
        return "Invalid email"
    if DB[email]["password"] == password:
          return f"Welcome back {DB[email]["name"]}!"
    else:
         return"Invalid password"
     
          
print(register("gayathri", "gayathri@gmail.com", "gay43526"))
print(register("Ganga", "gayathri@gmail.com", "gay43526"))
print(register("gayathri", "gayathri@g", "gay43526"))
print(register("ganga", "ganga@gmail.com", "gan9766d6"))

print(login("gayathri@gmail.com", "gay43526"))
print(login("gayathri@gmail.com", "87w89dh"))
print(login("gayi@gmail.com", "gay43526"))


                
        
    