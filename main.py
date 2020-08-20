def say_hello(username):
  if auth():
    print(f"Hello {username}")
  else:
    print(f"Hello guest, please log in.")

def main():
  try:
    from my_top_secret_data import auth
    username = input("What is your username?\n")
    say_hello(username)
  except:
    print("Incorrect username. Try again or sign in.")

if __name__ == "__main__":
  main()
  print("Hi She Codes!")
  print("Goodbye!")
  
