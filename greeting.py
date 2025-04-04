def greet(name):
  """Greets the person passed in as a parameter."""
  print(f"Hello, {name}! How are you today?")

if __name__ == "__main__":
  user_name = input("Enter your name: ")
  greet(user_name)
