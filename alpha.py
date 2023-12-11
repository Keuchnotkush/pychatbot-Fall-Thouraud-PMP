Sen = "Oppenheimer , POURQUOI !? , pas nominé aux Oscars dans la catégorie meilleurs effets visuels"
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
def token(sentence):
    L = []
    n = ""
    for o in sentence.split(" "):
        if all(z not in punc for z in o):
            n += o + " "
    n = n.lower()
    L = n.split(" ")
    return L
print(token(Sen))

