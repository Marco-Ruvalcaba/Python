def normalized(word):
    word = word.lower()
    word = word.replace(",","")
    word = word.replace(".","")
    return word

def Linear(string):
    dictionary = {}
    List = string.split()
    for word in List:
        if normalized(word) in dictionary:
            dictionary[normalized(word)] += 1
        else:
            dictionary[normalized(word)] = 1
    return dictionary


def Quadratic(string):
    List = string.split()
    CheckList = []
    counter = 0
    for word1 in List:
        CheckList.append( 0 )
        for word2 in List:
            if normalized(word1) == normalized(word2):
                CheckList[len(CheckList)-1] += 1
    return CheckList

string = "Hola, mucho gusto solo queria pasar a decir hola y saber como estas PERO NADA Hola, mucho gusto solo queria pasar a decir hola y saber como estas"
print("Linear: ", Linear(string))

print("Quadratic: ", Quadratic(string))
