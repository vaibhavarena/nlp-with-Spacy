import spacy

nlp = spacy.load('en_core_web_md')

text = 'A paragraph is a series of related sentences developing a central idea, called the topic. Try to think about paragraphs in terms of thematic unity: a paragraph is a sentence or a group of sentences that supports one central, unified idea. Paragraphs add one idea at a time to your broader argument.'

doc = nlp(text)

print(nlp.pipe_names)
print(nlp.pipeline)

for i in doc.noun_chunks:
    print(i)