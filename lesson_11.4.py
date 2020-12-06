string = 'DC makes good movies, DC makes good comics'
first = 'DC'
second = 'Marevel'

def change_name(string, first, second):
    for i in range(len(string)):
        if first == string[i:i+len(first)]:
            string = string[:i] + second + string[i+len(first):]
    return string

print(change_name(string, first, second))
