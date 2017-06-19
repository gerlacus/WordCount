# Word Count Tool
This is a word count tool that parses a play's script, counting how many times each character speaks any word. 
Using regular expressions, this program will determine whether a given line of text is a character's name, a line of dialogue being spoken, and initial scene setup + stage directions.
It will then produce a formatted writeup of its findings, listing each character, the words they spoke, and how many times they spoke each word. 
The results are printed to the console and into an external CSV file by the name of "wordcount.csv".

### Methodology
The general approach to this project began with understanding that the regex scripts needed to be able to distinguish between characters, lines, and stage directions.
This program is limited in the sense that it assumes the following of the text file passed in as a command-line argument:
* That character names are at the beginning of the line and one word long (i.e. no spaces)
* That dialogue is indented with some number of spaces greater than zero
* That stage directions and initial scene exposition are at the beginning of the line and more than one word long

With these constraints, I was able to successfully distinguish between these three groups on strictly a text-parsing basis.
From there, it was simply a matter of figuring out what to do with the information I had gathered.
In the end, I decided to use a nested dictionary implementation in { character name : { word spoken : frequency } } form to keep track of all relevant information. 

### Looking Forward
If I were to expand this application, I would certainly make it smarter at detecting a larger variety of formatting in the play scripts being passed in;
at the moment, it only works under the specific guidelines described above.
More versatility and adaptability would be necessary if I were to use the program in any plausible real-world situations.

Future endeavors might also include a GUI (likely built through PyQt) that would allow the tables of information to be presented in a more user-friendly manner than mere console output/CSV, whether it be through nested menus, better formatting, or any other means.

All in all, it was fun to work on a small project to jog my memory on regular expressions and Python's file I/O structures.

--Gerlacus
