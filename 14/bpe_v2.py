input = "ABCDCDABCDCDE"

tokens=list(input.encode("utf8"))
print("tokens",tokens)

next_token_id =256
new_tokens=[]
counts = {}
i = 0
pair_size=2
for index in range(len(tokens)-1) :
  pairs=tokens[index:index+pair_size]
  counts[tuple(pairs)] = counts.get(tuple(pairs),0) +1

max_pair=max(counts, key=counts.get)



while i < len(tokens):
  if tuple(tokens[i:i + pair_size]) == max_pair:
    new_tokens.append(next_token_id)    
    i += pair_size
  else:
    new_tokens.append(tokens[i])
    i += 1

next_token_id +=1
print("new_tokens",new_tokens)



next_token_id =256
new_tokens=[]
counts = {}

pair_size=2
def BPE(input):
  i = 0
  tokens=list(input.encode("utf8"))
  for index in range(len(tokens)-1) :
    pairs=tokens[index:index+pair_size]
    counts[tuple(pairs)] = counts.get(tuple(pairs),0) +1
  max_pair=max(counts, key=counts.get)

  while i < len(tokens):
    if tuple(tokens[i:i + pair_size]) == max_pair:
      new_tokens.append(next_token_id)
      i += pair_size
    else:
      new_tokens.append(tokens[i])
      i += 1
  return new_tokens


print(BPE("ABCDCDABCDCDE"))

