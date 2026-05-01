class Node:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
        self.originalWord = None

    #Checks if the word is already in the trie, if not adds it and returns the child node
    def addChild(self, char):
        if char not in self.children:
            self.children[char] = Node()
        return self.children[char]
    #Returns the child node for the given character, or None if it doesn't exist
    def getChild(self, char):
        return self.children.get(char)


class Trie:
    def __init__ (self):
        self.root = Node()
    
    def insert(self, word):
        if not word:
            return
        #converts the word to uppercase for suggestions
        node = self.root
        upper = word.upper()
        for char in upper:
            node = node.addChild(char)
        #Marks the end of the word and stores the original word for suggestions
        node.isEndOfWord = True
        node.originalWord = word

    def loadFile(self, filename = "MP_wordbank.txt"):
        #Loads the words from the file and inserts them into the trie. If the file is not found then it handles that through error message.
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    #Strips the line to get the word and inserts any non empty lines into the trie
                    word = line.strip()
                    self.insert(word)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        
    def suggestions(self, prefix, max_suggestions=5):
        #if its empty return empty list
        if not prefix:
            return []
        #traverses the trie for the uppercase version of the prefix
        node = self.root
        for char in prefix.upper():
            node = node.getChild(char)
            if node is None:
                return []
        #Gets the top 5 suggested words    
        results = []
        self._collect_words(node, results, max_suggestions)
        return results
    #Recursively gets the complete words until it reaches 5
    def _collect_words(self, node, results, limit):
        if len(results) >= limit:
            return

        if node.isEndOfWord and node.originalWord:
            results.append(node.originalWord)
        #Tims sort by using sorted()
        for char, child in sorted(node.children.items()):
            self._collect_words(child, results, limit)
#Loads the words from the file
class WordBank:
    def load(self, filename = "MP_wordbank.txt"):
        trie = Trie()
        trie.loadFile(filename)
        return trie

class CodeCompleter:
    def __init__(self):
        self.wordbank = WordBank()
        self.trie = self.wordbank.load()
        self.max_suggestions = 5

    def getSuggestions(self, current_input):
        words = current_input.strip().split()
        if not words:
            return []
        prefix = words[-1]
        return self.trie.suggestions(prefix, self.max_suggestions)
    
    def newWord(self, word):
        clean = word.strip()
        if len(clean) < 3:
            return
        
        if not any(clean.upper() == w.upper() for w in self.trie.suggestions(clean, 10)):
            self.trie.insert(clean)
            print(f"      [Learned new word: {clean}]")

    def acceptSuggestion(self, selected):
        return selected
    
def main():
    print("Code Completer - Type your code and get suggestions. Type 'exit' to quit.")
    print("Type your code. Press ENTER to get suggestions.")
    print("Type a word then ENTER to learn it if it's new.")
    print("Type 'EXIT' to quit.\n")

    completer = CodeCompleter()
    code_lines = []

    while True:
        user_input = input(">>> ").strip()

        if user_input.upper() == "EXIT":
            break

        suggestions = completer.getSuggestions(user_input)

        if suggestions:
            print("Suggestions:")
            for i, suggestion in enumerate(suggestions, 1):
                print(f"  {i}. {suggestion}")
            choice = input("Select a suggestion by number, or press ENTER to continue: ").strip()
            if choice.isdigit() and 1<= int(choice) <= len(suggestions):
                chosen = completer.acceptSuggestion(suggestions[int(choice)-1])
                print(f"     -> Inserted: {chosen}")
                code_lines.append(chosen)
                continue
        else:
            print("No suggestions found.")

        if user_input:
            last_word = user_input.split()[-1]
            completer.newWord(last_word)
            code_lines.append(user_input)

        print(f"       Current code: {' '.join(code_lines)}\n")

    print("\nFinal code:")
    print("\n".join(code_lines))

if __name__ == "__main__":
    main()