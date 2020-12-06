s_email = 'somebody_email@gmail.com'
a = '***@***'
s = s_email.index('@')

def change_name(s_email, s):
    for i in s_email:
        if i == '@':
            s_email = s_email[:s-5] + a + s_email[s+5:]
    return s_email

print(change_name(s_email, s))

