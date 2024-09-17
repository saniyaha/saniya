# Saniya Harrigan @03020812

class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = []

    # getit helper function to explore the grid (formerly dfs)
    def getit(self, row, col, visited, word, dict_set, prefix_set):
        rows, cols = len(self.grid), len(self.grid[0])

        # if out of bounds or already visited
        if row < 0 or col < 0 or row >= rows or col >= cols or visited[row][col]:
            return

        # Aad the current letter to the word
        current_char = self.grid[row][col]
        word += current_char

        # handle the "Qu" case
        if current_char == 'Qu':
            word += 'u'

        # if the word is not a valid prefix, return early
        if word.lower() not in prefix_set:
            return

        # Mark this cell as visited
        visited[row][col] = True

        # if the word is at least 3 letters and is in the dictionary, add to solutions
        if len(word) >= 3 and word.lower() in dict_set:
            self.solutions.append(word)

        # explore all 8 directions (diagonals included)
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        for dx, dy in directions:
            self.getit(row + dx, col + dy, visited, word, dict_set, prefix_set)

        # unmark this cell as visited for backtracking
        visited[row][col] = False

    # method to find all solutions
    def getSolution(self):
        if not self.grid or not self.dictionary:
            return []

        # create sets for dictionary and prefixes
        dict_set = self.create_dictionary_set(self.dictionary)
        prefix_set = self.create_prefix_set(self.dictionary)

        rows, cols = len(self.grid), len(self.grid[0])
        self.solutions = []

        # start getit from each cell
        for i in range(rows):
            for j in range(cols):
                visited = [[False for _ in range(cols)] for _ in range(rows)]
                self.getit(i, j, visited, '', dict_set, prefix_set)

        # return unique solutions (set removes duplicates)
        return list(set(self.solutions))

    # helper method to create a set of valid dictionary words
    def create_dictionary_set(self, dictionary):
        return {word.lower() for word in dictionary if len(word) >= 3}

    # helper method to create a set of valid prefixes
    def create_prefix_set(self, dictionary):
        prefix_set = set()
        for word in dictionary:
            prefix = ''
            for char in word:
                prefix += char.lower()
                prefix_set.add(prefix)
        return prefix_set

def main():
    grid = [["T", "W", "Y", "R"],
            ["E", "N", "P", "H"],
            ["G", "Z", "Qu", "R"],
            ["O", "N", "T", "A"]]

    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", 
                  "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", 
                  "ten", "went", "wet", "arty", "rhr", "not", "quar"]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()
