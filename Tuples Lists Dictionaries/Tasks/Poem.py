import random

def word_generation(list_words):
    '''Generation word from list'''
    new_word = random.choice(list_words)
    list_words.pop(list_words.index(new_word))
    return new_word

#list of wors
nouns = ['fossil','horse','aardvark','judge','chef','mango','extrovert','gorilla']
verbs = ['kicks','jingles','bounces','slurps','meows','explodes','curdles']
adjectives = ['furry','balding','incredulous','fragrant','exuberant','glistening']
prepositions = ['against','after','into','beneath','upon','for','in','like','over','within']
adverbs = ['curiously','extravagantly','tantalizingly','furiously','sensuously']

choosed_nouns = []
choosed_verbs = []
choosed_adjectives = []
choosed_prepositions = []
choosed_adverbs = []

#Generations words for POEM
while len(choosed_nouns) != 3:
    choosed_nouns.append(word_generation(nouns))

while len(choosed_verbs) != 3:
    choosed_verbs.append(word_generation(verbs))

while len(choosed_adjectives) != 3:
    choosed_adjectives.append(word_generation(adjectives))

while len(choosed_prepositions) != 2:
    choosed_prepositions.append(word_generation(prepositions))

choosed_adverbs.append(word_generation(adverbs))

#Generation POEM

print(f'''A {choosed_adjectives[0]} {choosed_nouns[0]}
A {choosed_adjectives[0]} {choosed_nouns[0]} {choosed_verbs[0]} {choosed_prepositions[0]} the {choosed_adjectives[1]} {choosed_nouns[1]}
{choosed_adverbs[0]}, the {choosed_nouns[0]} {choosed_verbs[1]}
the {choosed_nouns[1]} {choosed_verbs[2]} {choosed_prepositions[1]} a {choosed_adjectives[2]} {choosed_nouns[2]}'''
)



