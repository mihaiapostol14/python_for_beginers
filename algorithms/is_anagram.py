def is_anagram(test:str, original:str):
    return sorted(test.lower().replace(' ','')) == sorted(original.lower().replace(' ',''))
