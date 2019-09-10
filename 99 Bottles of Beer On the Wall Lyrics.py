"""
Project Challenge: Create a program that prints out every line in the song '99 Bottles of Beer on the Wall'. 

Rules:
    - Cannot manually type out all the lines.
    - Can use a list for numbers but cannot manually type them all in..
    - Put a blank line between each verse of the song.
    - Cannot type in any numbers/names of numbers diretly into the lyrics.
"""

def main():
    lines = [];
    for i in range(99, 0, -1):
        verse = "";
        if i == 1:
            verse = str(i) + " bottle of beer on the wall, " + str(i) + " bottle of beer! \n You take one down, pass it around, " + str(i - 1) + " bottles of beer on the wall \n";
        else:
            verse = str(i) + " bottles of beer on the wall, " + str(i) + " bottles of beer! \n You take one down, pass it around, " + str(i -1) + " bottles of beer on the wall \n";
        lines.append(verse)
    for j in lines:
        print(j);
        
main()