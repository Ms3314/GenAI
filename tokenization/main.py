# we will use an library called tik tokens 
import tiktoken 
enc = tiktoken.encoding_for_model("gpt-4o")
text = "Hello , this is Sami"
tokens = enc.encode(text)
print("Tokens:",tokens)


tokens = [13225, 1366, 495, 382, 169256]
decoded = enc.decode(tokens)
print(decoded , "This is Decoded")