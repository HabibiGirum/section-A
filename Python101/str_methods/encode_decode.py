text = "Hello café"

# Default UTF-8(Universal Standard) encoding
print(text.encode())  # b'Hello caf\xc3\xa9' (é becomes 2 bytes)

# ASCII(English only) encoding (can't handle é)
print(text.encode("ascii", errors="ignore"))  # b'Hello caf'
print(text.encode("ascii", errors="replace"))  # b'Hello caf?'

# Converting back
encoded = text.encode()
decoded = encoded.decode("utf-8")
print(decoded)  # "Hello café"