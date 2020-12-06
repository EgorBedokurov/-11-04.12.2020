string = input('enter some string ')

def search(string):
    st = string.split()
    count = 0
    for i in st:
        if len(i) > count:
            count = len(i)
            word = i
    return word

print('the longest word is: ' + search(string))