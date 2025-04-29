from Login import register, login

def test_cases():
    assert register("gayathri", "gayathri@gmail.com", "gay43526") == "Registeration successfull"

    assert register("Ganga", "gayathri@gmail.com", "gay43526") == "Email already exists"

    assert register("gayathri", "gayathri@g", "gay43526") == "Invalid email"

    assert register("ganga", "ganga@gmail.com", "gan9766d6") == "Registeration successfull"


    assert login("gayathri@gmail.com", "gay43526") == "Welcome back gayathri!"

    assert login("gayathri@gmail.com", "87w89dh") == "Invalid password"

    assert login("gayi@gmail.com", "gay43526") == "Invalid email"


test_cases()
print("all test cases passed")