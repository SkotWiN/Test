irregular_verbs = ['be', 'beat', 'become', 'begin', 'bleed', 'blow', 'break', 'bring', 'build', 'burst', 'buy',
'catch', 'choose', 'come', 'cost', 'creep', 'cut',
'do', 'draw', 'dream', 'drink', 'drive',
'eat',
'fall', 'feed', 'feel', 'fight', 'find', 'fit', 'fly', 'forget', 'forgive', 'freeze',
'get', 'give', 'go', 'grow',
'hang', 'have', 'hear', 'hide', 'hit', 'hold', 'hurt',
'keep', 'kneel', 'know',
'lay', 'lead', 'lean', 'learn', 'leave', 'lend', 'let', 'lie', 'light', 'lose',
'make', 'meet', 'mistake',
'pay', 'prove', 'put',
'quit',
'read', 'ride', 'ring', 'rise', 'run'
'say', 'see', 'seek', 'sell', 'send', 'set', 'sew', 'shake', 'show', 'shrink', 'shut', 'sing', 'sink', 'sit',
'sleep', 'slide', 'sow', 'speak', 'spell', 'spend', 'spoil', 'spread', 'spring', 'stand', 'steal', 'stick',
'sting', 'sweep', 'swell', 'swim',
'take', 'teach', 'tear', 'tell', 'think', 'throw',
'undestand',
'wake', 'wear', 'weep', 'wet', 'win', 'wind', 'write']
your_verb_to_be_checked = input("Ввести свой глагол: ")
if your_verb_to_be_checked in irregular_verbs:
    print('That is an irregular verb')
else:
    print('That is a regular verb')

input()