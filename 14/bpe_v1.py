input = "ABCDCDABCDCDE"

tokens=list(input.encode("utf8"))

print("tokens : ",tokens)

i = 0
n = 1
maxID =256
max_pair=[]
new_tokens=[]
for token in tokens :
  n=n+1
  pairs=tokens[i:n]

  if n == len(tokens) :
    break
  i=i+1
  count = 0
  for ii in range(len(tokens) - len(pairs)+1):
    if tokens[ii:ii + len(pairs)] == pairs:
      count += 1
      counts = {}
      counts[tuple(pairs)] = count
      max_pair = max(counts, key=counts.get)
iii = 0
maxID +=1
while iii < len(tokens):
  if tuple(tokens[iii:iii + 2]) == max_pair:
    new_tokens.append(maxID)    
    iii += 2
  else:
    new_tokens.append(tokens[iii])
    iii += 1
print("new_tokens",new_tokens)