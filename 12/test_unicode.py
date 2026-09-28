text = "Hello, 🌍! こんにちは!"

tokens = [ord(c) for c in text]

num_bytes = len(text.encode("utf-8"))
token_count = len(tokens)
vocab_size = max(tokens) + 1
compression_ratio = num_bytes / token_count

print("=== Unicode tokenizer ===")
print("text:", text)
print("tokens:", tokens)
print("UTF-8 bytes:", num_bytes)
print("token count:", token_count)
print("vocabulary size:", vocab_size)
print("compression ratio:", compression_ratio)