def is_palindrome(word):
	word = word.lower()
	return word == word[::-1]


def find_palindromes(words):
	palindromes = []

	for word in words:
		if is_palindrome(word):
			palindromes.append(word)

	return palindromes
