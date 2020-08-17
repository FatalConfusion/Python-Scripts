#taking input of the string and converting it to list
init_string=input("Enter the string you wanna reverse: ")
initial_string=init_string.split(" ")

#reversing the list using 'reversed' and then converting it back to a normal string using join  
reversed_string_by_words=list(reversed(initial_string))
reversed_string_by_words=" ".join(reversed_string_by_words)
print("reversed string by words: %s"%reversed_string_by_words)

#a senseless reverse
senseless_reverse=init_string[::-1]
senseless_reverse2="".join(init_string)
print("senseless reverse: %s"%senseless_reverse)
print("one more senseless reverse: %s"senseless_reverse2)
