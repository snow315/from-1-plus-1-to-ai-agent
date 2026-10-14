input = "ABCDCDABCDCDE"

print("input : ",input)


tokens=list(input.encode("utf8"))

print("old_tokens : ",tokens)

print("-------------------------------------------------")
next_token_id =256
pair_size=2

def BPE(tokens_from_utf8,next_token_id):
  new_tokens=[]
  tokens_from_utf8_len = len(tokens_from_utf8)  
  counts = {}
  i = 0
  
  for index in range(tokens_from_utf8_len-1) :
    pairs=tokens_from_utf8[index:index+pair_size]
    counts[tuple(pairs)] = counts.get(tuple(pairs),0) +1

  max_pair=max(counts, key=counts.get)
  
  while i < tokens_from_utf8_len:

    if tuple(tokens_from_utf8[i:i + pair_size]) == max_pair:
      new_tokens.append(next_token_id)
      i += pair_size
    else:
      new_tokens.append(tokens_from_utf8[i])
      i += 1
  
  return new_tokens,next_token_id,max_pair

def decode(tokens, tokens_table):
    new_tokens = tokens.copy()

    for k in sorted(tokens_table.keys(), reverse=True):
        result = []

        for token in new_tokens:
            if token == k:
                result.extend(tokens_table[k])
            else:
                result.append(token)

        new_tokens = result

    return new_tokens


#BEP_01,next_token_id_01,max_pair_01 = BPE(tokens,next_token_id+1)
#rint(BEP_01)
#tokens_table[next_token_id_01] =max_pair_01
#print("--------------------------")


#BEP_02,next_token_id_02,max_pair_02  = BPE(BEP_01,next_token_id_01+1)
#print(BEP_02)
#tokens_table[next_token_id_02] =max_pair_02
#print("--------------------------")

#print("decode_next_token_id_01 : ",next_token_id_01,"=",decode(tokens_table,next_token_id_01))
#print("decode_next_token_id_02 : ",next_token_id_02,"=",decode(tokens_table,next_token_id_02))



tokens_table= {}
new_token= []
def loop_BPE(tokens,next_token_id,n):

  token_ids=0
  max_pair=()
  if n == 0:
    #print("===========")

    return tokens,tokens_table
    
  else:
    
    new_token,token_ids,max_pair = BPE(tokens,next_token_id)
    #print("-------------------------------------------------")
    #print("loop_BEP_n :",n)
    print("BPE_new_tokens :",new_token)
    print("BPE_new_token_ids :",token_ids,",BPE_pair :",max_pair)
    print("-------------------------------------------------")
    #print("loop_BEP_max_pair :",max_pair)
    tokens_table[token_ids] =max_pair


    next_token_id +=1
    return loop_BPE(new_token,next_token_id,n-1)





new_token,tokens_table=loop_BPE(tokens,next_token_id,3)


#print("after_BPE : ",new_token)
#print("==========================")
#for k, v in tokens_table.items():
#  print("tokens_ID : ",k,",tokens : ",v)

after_decode = decode(new_token,tokens_table)
print("new_tokens : ",after_decode )

output = bytes(after_decode).decode("utf-8")

print("output : ", output )

print("old_tokens = new_tokens ? ",tokens==after_decode)
print("input = output ? ",input == output)







