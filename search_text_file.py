words = [ 'word1', 'word2', 'foo']

daSearch = open("foo.txt", "r").read()

for word in words:
    if word in daSearch:
       print(word)
    else:
       print("not found")

print("\nDone")
