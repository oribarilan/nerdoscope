def stream_print(chain, context):
    # This function will stream the output of the chain and print it in a readable way for the notebook
    word_count = 0
    buffer = ""

    for s in chain.stream(context):
        buffer += s
        words = buffer.rsplit(' ', 1)
        if len(words) > 1:
            for word in words[:-1]:
                print(word, end=' ', flush=True)
                word_count += 1
                if word_count == 10:
                    print()
                    word_count = 0
            buffer = words[-1]
    if buffer:
        print(buffer, end='', flush=True)
    print()
