text = input("文字列を入力してください: ")

byte_length = len(text.encode("utf-8"))

print(f"文字数: {len(text)}")
print(f"UTF-8 バイト数: {byte_length}")
