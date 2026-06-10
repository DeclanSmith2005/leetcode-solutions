class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        mapping = {k : v for k, v in replacements}
        def convert(string):
            markers = []
            newString = ""
            for i in range(len(string)):
                if string[i] == '%':
                    markers.append(i)
            prev = 0
            newString = ''
            for i in range(0, len(markers), 2):
                start, end = markers[i], markers[i+1]
                newString += string[prev:start]
                newString += convert(mapping[string[start+1 : end]])
                prev = end +1
            newString += string[prev:]
            return newString
        return convert(text)
        

