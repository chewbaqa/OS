with open('example.txt','w') as file:
    file.write("Hello i am Vishal")

with open('example.txt','r') as file:
    file.seek(5)    
    content = file.read()
    print(content)
    file.close()
