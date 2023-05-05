import random
 
 
def main():
    n = random.randint(0, 10)
    generate_files(0, '', 2, n)  # file 0
 
    filename = "books_10.txt"
    infix = generate_infix(filename, True)  # file 1
    generate_files(1, infix, 1, 0)  # full title infix, binary search tree, all bestsellers
    infix = generate_infix(filename, True)  # file 2
    generate_files(2, infix, 2, 0)  # full title infix, binary heap, all bestsellers
 
    infix = generate_infix(filename)
    n = random.randint(4, 8)
    generate_files(3, infix, 1, n)  # infix, binary search tree, top n bestsellers
 
    infix = generate_infix(filename)
    n = random.randint(4, 8)
    generate_files(4, infix, 2, n)  # infix, binary search tree, top n bestsellers
 
 
def generate_files(filenum, infix: str, datastructure: int, n: int):
    file_fb = open(f"feedback_{filenum}.txt", "w")  # file with infix for feedback
    file_fb.write("Testing Bookstore System Option 9 using...\n")
    file = open(f"bookstore_input_{filenum}.txt", "w")  # input with infix
    file.write('2\n')
    file.write('1\n')
    file.write('books_10.txt\n')
    file.write('9\n')
    # infix
    file.write(infix + '\n')
    file_fb.write("\n\t- Infix: \"" + infix + "\"")
 
    # data structure
    file.write(f'{datastructure}\n')
    file_fb.write(f"\n\t- Data structure: {datastructure}")
 
    # count
    if n == 0:
        file_fb.write(f"\n\t- Number of top bestsellers: {n} (all matches)")
    else:
        file_fb.write(f"\n\t- Number of top bestsellers: {n}")
    file.write(str(n) + '\n')
 
    file_fb.close()
 
    file.write('0\n')
    file.write('0\n')
    file.close()
 
 
def generate_infix(filename: str, full_title=False) -> list:
    file = open(filename, encoding="utf8")
    catalogue = list(file.readlines())
    file.close()
    num_books = len(catalogue)
    idx = random.randint(0, num_books - 1)
    book = catalogue[idx]
    (key, title, group, rank, similar) = book.split("^")
    while len(title) < 20:
        idx = random.randint(0, num_books - 1)
        book = catalogue[idx]
        (key, title, group, rank, similar) = book.split("^")
 
    if full_title:
        return title
    else:
        start = random.randint(0, len(title) - 15)
        end = start + random.randint(8, 10)
        infix = title[start: end]
        return infix
 
 
if __name__ == "__main__":
    main()
 