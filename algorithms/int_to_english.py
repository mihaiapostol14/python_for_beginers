def int_to_english(n):
    if n == 0:
        return "zero"

    below_20 = ["", "one", "two", "three", "four", "five", "six", "seven",
                "eight", "nine", "ten", "eleven", "twelve", "thirteen",
                "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                "nineteen"]

    tens = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]

    thousands = ["", "thousand", "million", "billion", "trillion", "quadrillion",
                 "quintillion", "sextillion", "septillion"]

    def three_digit_to_words(num):
        hundred = num // 100
        rest = num % 100
        parts = []

        if hundred > 0:
            parts.append(below_20[hundred])
            parts.append("hundred")

        if rest > 0:
            if rest < 20:
                parts.append(below_20[rest])
            else:
                parts.append(tens[rest // 10])
                if rest % 10:
                    parts.append(below_20[rest % 10])

        return " ".join(parts)

    words = []
    chunk_index = 0

    while n > 0:
        chunk = n % 1000
        if chunk != 0:
            chunk_words = three_digit_to_words(chunk)
            if thousands[chunk_index]:
                chunk_words += " " + thousands[chunk_index]
            words.append(chunk_words)
        n //= 1000
        chunk_index += 1

    return " ".join(reversed(words)).strip()

print(int_to_english(42))           # "forty two"
print(int_to_english(123456789))    # "one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine"
print(int_to_english(10**21))       # "one sextillion"
