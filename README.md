# Google-auto-complete-project

Google Project (~30h challenge) : Search and auto-completion for sentences within given input text files.Manipulating the data with complex data-structures and algorithmic optimizations using Python

introduction:
In order to improve the user experience of the Google search engine, the development team decided to allow the completion of sentences from articles, documentation and information files on various technological topics.
The program supports two main functions:
● Initial function - the function receives a list of text sources on which the search engine will run, each source contains a collection of sentences. The function saves the results in the best way for the benefit of the completion function - in a trie that contains all the sentences and sub sentences and at the end of each word there is a list of all the sentences that contain the sentence obtained from a route in the trie from the root to the end of the word. This list is written into a file to save memory from the ram.
● Completion function - the function receives a string - which is the text that the user typed - the function returns the five best completions (good completion will be defined later).

The completion:
The purpose of the completion action is to make it easier for the user to find the most appropriate sentence.
We will set a match between a sentence and text that the user typed if:
● The text is a sub-string of the sentence (it includes the beginning, middle or end of the sentence).
● Text in which if we make one correction then the text will form a sub-string of the sentence.

Correction is defined as:
● Character replacement
○ Example: The string "to be not to by" is considered a sub-string of the text "to be or not to be so is the question", with the substitution of the character "y" in the word "by" for "e".
● Delete a character.
○ Example: The string "to be or nt" is considered a sub-string of the text "to be or not to be that is the question", with the deletion of the character "o" in the word "not".
● Add a character.
○ Example: The string "to bee or not" is considered a sub-string of the text "to be or not to be is the question", with the addition of the character "e" in the word "be".

match score:
In the case of multiple matches to the typed text, we will set a score for each match:
● The base score is double the number of characters typed and a match was found for them.
● Replacement a character reduces the score according to the following: first character 5 points, second character 4, third character 3, fourth character 2, fifth character and so on 1.
● Deleting a character or adding a character receives a reduction of 2 points except for the first 4 characters) first character 10 points, second character 8, third character 6, fourth character 4

Input and output notes:
● The text files are stored in a folder tree structure and are in the Archive folder
● The texts are placed at different heights in the tree, meaning a text file can be inside a folder, inside a folder inside a folder, and so on.
● The user does not need to type uppercase / lowercase letters, punctuation while typing the input text, in addition there is no limit to the number of spaces between the words. That is, if the original sentence is "to be or not to be, that is the question" - then even if the user typed "to be that", "to be, that" or "to be       this" then the system must treat the three sub-strings as same.
● The output of the system is a line from the source files in its original form) i.e. includes punctuation (and the path of the file).
