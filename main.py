with open("books/frankenstein.txt") as f:
  file_contents = f.read()
  words = file_contents.lower().split()

  print("--- Begin Report of books/frankenstein.txt ---")
  count = len(words)
  print(f"{count} words found in the document")
  print("")
  count_of_letters = {}
  #letters_list = ["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  
  for letter in file_contents.lower():
    if letter in count_of_letters:
      count_of_letters[letter]+= 1
    else:
      count_of_letters[letter] = 1
  
  list_of_dicts = []
  def sort_on(d):
    return d["count"]
  
  
  for letter, count in count_of_letters.items():
    list_of_dicts.append({"letter": letter, "count": count})
  
  list_of_dicts.sort(key=sort_on, reverse=True)

  for item in list_of_dicts:
    print(f"The {item['letter']} character was found {item['count']} times")
  

  
  print("--- End report ---")
  
  
  
  
  