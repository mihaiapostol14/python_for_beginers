import re


def get_hashtags(string: str = '', filename: str = 'hashtags.txt'):
    hashtags = re.findall(r'#\w+', string, re.UNICODE)
    unique_hashtags = sorted(set(hashtags))  #  remove duplicates and sort

    with open(filename, 'w', encoding='utf-8') as f:
        for tag in unique_hashtags:
            f.write(tag + '\n')  # write each hashtag on a new line

    return unique_hashtags  # return the result if necessary

