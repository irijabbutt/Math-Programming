# occurences of a specific character in a string
def count_character_occurrences(string, char):
 return string.count(char)
test_string = "hello world"
char_to_count = "l"
print("Occurrences of", char_to_count, "in", test_string, ":",
count_character_occurrences(test_string, char_to_count))