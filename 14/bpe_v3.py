input = "ABCDCDABCDCDE"
tokens=list(input.encode("utf8"))

print("old_tokens : ",tokens)
next_token_id =256
pair_size=2

tokens_table= {}


def BPE(tokens_from_utf8,next_token_id):
  new_tokens=[]
  tokens_from_utf8_len = len(tokens_from_utf8)  
  counts = {}
  i = 0
  
  for index in range(tokens_from_utf8_len-1) :
    pairs=tokens_from_utf8[index:index+pair_size]
    counts[tuple(pairs)] = counts.get(tuple(pairs),0) +1
    

  max_pair=max(counts, key=counts.get)

  print(tokens_from_utf8_len)
  while i < tokens_from_utf8_len:
    print("BPE : ",i)
    print("BPE : ",tokens_from_utf8[i:i + pair_size])
    print("BPE : ",max_pair)
    if tuple(tokens_from_utf8[i:i + pair_size]) == max_pair:
      
      new_tokens.append(next_token_id)
      print("^^^^^^^^^^^^^^^^^^")
      i += pair_size
    else:
      new_tokens.append(tokens_from_utf8[i])
      i += 1
    return new_tokens,next_token_id,max_pair




 


BEP_01,next_token_id_01,max_pair_01 = BPE(tokens,next_token_id+1)
print("BEP_01 : ",BEP_01)
#tokens_table[next_token_id_01] =max_pair_01

#BEP_02,next_token_id_02 ,max_pair_02 = BPE(BEP_01,next_token_id_01+1)
#print("BEP_02 : ",BEP_02)
#tokens_table[next_token_id_02] =max_pair_02

#BEP_03,next_token_id_03 ,max_pair_03 = BPE(BEP_02,next_token_id_02+1)
#print("BEP_03 : ",BEP_03)
#tokens_table[next_token_id_03] =max_pair_03


#print("tokens_table : ",tokens_table)

#print("decode_next_token_id_01 : ",next_token_id_01,"=",decode(tokens_table,next_token_id_01))
#print("decode_next_token_id_02 : ",next_token_id_02,"=",decode(tokens_table,next_token_id_02))
#print("decode_next_token_id_03 : ",next_token_id_03,"=",decode(tokens_table,next_token_id_03))

def decode(tokens_table,token_id):
  token = [v for k, v in tokens_table.items() if k == token_id]
  return token

def loop_BEP(tokens,token_id,n):
  print("loop_BEP :",tokens)
  print("loop_BEP :",token_id)
  if n == 0:
    return new_tokens,token_ids,max_pair
  else:
    
    new_tokens,token_ids,max_pair = BPE(tokens,token_id+1)
    print(new_tokens)
  loop_BEP(new_tokens,next_token_id,n-1)

print("================")

print(loop_BEP(tokens,next_token_id+1,2))
   
   