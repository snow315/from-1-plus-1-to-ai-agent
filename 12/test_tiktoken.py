import tiktoken

text = "Hello, 🌍! こんにちは!"

enc = tiktoken.get_encoding("cl100k_base")

tokens = enc.encode(text)

num_bytes = len(text.encode("utf-8"))
token_count = len(tokens)
compression_ratio = num_bytes / token_count

print("=== BPE tokenizer ===")
print("text:", text)
print("tokens:", tokens)
print("UTF-8 bytes:", num_bytes)
print("token count:", token_count)
print("vocabulary size:", enc.n_vocab)
print("compression ratio:", compression_ratio)

#print("\nToken details:")
#for token_id in tokens:
#    token_bytes = enc.decode_single_token_bytes(token_id)
#    print(token_id, token_bytes)