def autocorrect(text: str ) -> str:
    correct = 'your client'
    wrong = ('youuuu', 'u', 'you')
    t_split = text.split()
    for s in t_split:
        if s in wrong:
            text = text.replace(s, correct)
            break
    if text.endswith(wrong):
        nr_sym = len(text.split()[-1])
        return f'{text[:-nr_sym - 1]} {correct}'
    else:
        return text

print(autocorrect(text="We have sent the deliverables to u"))
print(autocorrect(text="We have sent the deliverables to you"))
print(autocorrect(text="We have sent the deliverables to youuuu"))
print(autocorrect(text="youtube"))
