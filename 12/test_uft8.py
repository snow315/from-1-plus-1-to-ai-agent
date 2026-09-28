text = "Hello, 🌍! こんにちは!"

tokens = list(text.encode("utf-8"))

num_bytes = len(text.encode("utf-8"))
token_count = len(tokens)

# byte 只有 0~255
vocab_size = 256

compression_ratio = num_bytes / token_count

print("=== Byte tokenizer ===")
print("text:", text)
print("tokens:", tokens)
print("UTF-8 bytes:", num_bytes)
print("token count:", token_count)
print("vocabulary size:", vocab_size)
print("compression ratio:", compression_ratio)