import math
from collections import Counter


def char_probs(text):
    char_counts = Counter(text)
    total_chars = len(text)
    return {char: count / total_chars for char, count in char_counts.items()}


def entropy(probs):
    return -sum(p * math.log2(p) for p in probs.values())


def cond_entropy(text):
    char_counts = Counter(text)
    total_chars = len(text)

    cond_ent = 0
    for char in char_counts:
        count = char_counts[char]
        next_chars = [
            text[i + 1] for i in range(total_chars - 1) if text[i] == char
        ]
        next_probs = [nc / count for nc in Counter(next_chars).values()]
        cond_ent -= count * sum(p * math.log2(p) for p in next_probs)
    cond_ent /= total_chars

    return cond_ent


def main():
    with open("../data/text", "r") as file:
        text = file.read()

    shannon_entropy = entropy(char_probs(text))
    conditional_entropy = cond_entropy(text)
    mutual_info = shannon_entropy - conditional_entropy

    print(f"Shannon entropy: {shannon_entropy}")
    print(f"Conditional entropy: {conditional_entropy}")
    print(f"Mutual information: {mutual_info}")


if __name__ == "__main__":
    main()
