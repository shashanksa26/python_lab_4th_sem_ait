import random
import re

def generate_number():
  """Generates a random phone number."""
  return "+" + str(random.randint(100000000000, 999999999999))

def generate_gmail_id():
  """Generates a random Gmail ID."""
  return random.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]) + str(random.randint(1000000, 9999999)) + "@gmail.com"

def generate_5b_txt_file():
  """Generates a 5b.txt file containing random phone numbers and Gmail IDs."""
  with open("5b.txt", "w") as f:
    for i in range(50):
      f.write(generate_number() + "\n")
      f.write(generate_gmail_id() + "\n")

if __name__ == "__main__":
  generate_5b_txt_file()