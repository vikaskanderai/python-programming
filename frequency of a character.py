word=input("Enter any word")
def most_frequent(word):
    dict={}
    for i in word:
        keys=dict.keys()
        if i in keys:
            dict[i] +=1
        else:
            dict[i] =1
    return dict
d=(most_frequent(word))
a=sorted(d.items(), key=lambda x: x[1], reverse=True)
print(a)
