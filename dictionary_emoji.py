
msg=input(">")
split_msg=msg.split(" ")        #splitting on space
emoji={
    ":)":  "😀",
    ":(" : "😯",
    ":P" : "😛"
}
output=""
for word in split_msg:
    output+=emoji.get(word,word)+" " #if emoji is not there it will return that msg as it is
print(output)