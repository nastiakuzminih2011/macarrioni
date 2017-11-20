with open('text.txt', encoding='utf-8') as f:
    text = f.read()
for c in ['.',"'", '"', ':', '»', '«']:
    text = text.replace(c, "")
replaced_text = text.split()
x = 0
for word in replaced_text:
    print(word)
    if len(word) > 10:
        x = x + 1
print(x / len(replaced_text) * 100)
        
input("Done")