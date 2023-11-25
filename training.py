import preprocess

pos,neg = preprocess.read_data('data.json')

pos = preprocess.segment_words(pos)
neg = preprocess.segment_words(neg)

'''
print("Positive Reviews")
print(pos[:5])

print("Negative Reviews")
print(neg[:5])
'''

