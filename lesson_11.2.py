s_email = 'somebody_email@gmail.com'
a = '***'
b = ''
s = s_email.index('@')

def change_name(s_email, s):
    for i in s_email:
        if i == '@':
            s_email = s_email[:s-3:1] + a + '@' + s_email[s+1:] #+ a #+ s_email[]
            # cont += 1
    return s_email

print(change_name(s_email, s))