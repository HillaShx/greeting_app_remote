def say_hey(username):
  if auth():
    print(f"Hey {username}")
  else:
    print(f"Hey guest, please log in.")

def main():
  try:
    from my_top_secret_data import auth
    username = input("What is your username?\n")
    say_hey(username)
  except:
    print("Missing authentication module")

if __name__ == "__main__":
  main()
  
