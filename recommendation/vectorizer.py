def sentence_vectorizer(input_sentence):
    imsi = None
    for i in input_sentence:
        if imsi is None:
            imsi = i
        else:
            imsi += i
    

    return imsi / len(input_sentence)