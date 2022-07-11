def count_words():
  file = open("notes.txt")
  data = file.read()
  count = 0
  words = data.split()
  
  for word in words: 
    if word == "the" or word == "The": 
        count += 1
  return count

print(count_words())