with open('corpus.jsonl', 'a+') as out:
    with open('dataset.csv') as f:
        for line in f.read().splitlines():
            sentence = line[line.index(',') + 1:]
            sentence = sentence.replace('"', '')
            out.write('{"text": ' + '"' + sentence + '"}\n')
