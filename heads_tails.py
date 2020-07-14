ht = []
print('Enter h for heads, t for tails, or done when finished')
a = ''
c = 1

while a != 'done':
    a = input('Trial {}: '.format(c))
    if a == 'h' or a == 't':
        ht.append(a)
        c += 1
    else:
        if a == 'done':
            break
        else:
            print('NOT A VALID ENTRY')

al = len(ht)
h = ht.count('h')
t = ht.count('t')
hper = h/al*100
tper = t/al*100
print('\n')
print('Total trials: ',al)
print('Heads occured {}% of the time.'.format(hper))
print('Tails occured {}% of the time.'.format(tper))
