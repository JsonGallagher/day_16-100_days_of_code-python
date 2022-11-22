count = 1
word = "give"
guess = ""

print("Fill in the blank lyrics!")
print("Type in the blank lyrics and see if you are as cool as me.")

while True:
  if guess != word:
    guess = input("Never going to ____ you up ").lower()
    if guess != word:
      print("Nope, try again.")
      count += 1
  else:
    break
print(f"Well done! It only took you {count} attempt(s).")
