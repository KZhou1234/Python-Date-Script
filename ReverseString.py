#reverse the given string
#1. take the input using input()
#2. get the character start from the end of the string

words = input("Please enter a string.\n")
end = len(words) - 1
output = ""
for i in range (end, -1, -1):
    output += words[i]

print(output)