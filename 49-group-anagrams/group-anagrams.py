class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dico = dict()
        for word in strs:
            alphabet = [0]*26
            for letter in word:
                index = ord('a') - ord(letter)
                alphabet[index] += 1
            key = tuple(alphabet)
            if key in dico:
                dico[key].append(word)
            else: dico[key] = [word]

        return list(dico.values())


        