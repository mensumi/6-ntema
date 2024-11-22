from data import secret
# for i in range(len(secret)): 
   # print(secret[i])
#for i in secret:
  #  print(i)

# for i in secret:
#   if i[0] == "Океан":
#     print (f"слово - {i[0]},подсказка - {i[1]} ")
word = secret[5][0]
hide_word = ""
for i  in word:
  hide_word += "*"
print (hide_word)