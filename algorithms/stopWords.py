from collections import Counter
import re

def stopWords(text, k):
    # Basic list of English stopwords
    stop_words = {
        'the', 'is', 'in', 'and', 'to', 'a', 'of', 'that', 'it', 'on', 'for',
        'with', 'as', 'was', 'but', 'at', 'by', 'an', 'be', 'are', 'from', 'this',
        'or', 'which', 'you', 'we', 'they', 'he', 'she', 'his', 'her', 'them'
    }

    # Normalize the text: lowercase and extract words
    words = re.findall(r'\b[a-z]+\b', text.lower())

    # Remove stopwords
    filtered_words = [word for word in words if word not in stop_words]

    # Count frequencies of remaining words
    word_counts = Counter(filtered_words)

    # Get the k most common words
    top_k = [word for word, _ in word_counts.most_common(k)]

    return top_k

# Optional main block if you're testing locally
if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog. The dog was not amused."
    k = 3
    result = stopWords(sample_text, k)
    print(result)  # Example: ['dog', 'quick', 'brown']
