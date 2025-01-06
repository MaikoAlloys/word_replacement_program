def replace_waord():
    str="""The quick brown fox jumps over the lazy dog. 
    This sentence is an example often used to demonstrate all letters of the alphabet in a short phrase."""
    print(str)
    word_to_replace=input("Enter the word to replace: ")
    word_to_be_replaced=input("Enter the word to be replaced with: ")

    print(str.replace(word_to_replace,word_to_be_replaced))

replace_waord()