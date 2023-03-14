# User Manual

## Install `python`

First check if you have python installed by running `python`. If this opens an interactive python
environment you can skip this section.

Otherwise download and install the latest python version for macOS [here](https://www.python.org/downloads/).

## Create word lists

### With Quizlet

You can use [quizlet.com](quizlet.com) to create word lists as you would normally. Then you can
export them so they can be used with the program. Note that the script is designed to have you type
/ be tested on the "definition" part of the card. Terms should be unique otherwise the program will
on store the latest definition.

On a Quizlet set, click the three dots and then export. The settings should be:

- Between term and defintion: `Tab`
- Between rows: `New line`

You can then simply copy the text given and paste it into a text file on your computer. I recommend
using `vim`: simply type `vim <name of file>`, paste the contents, and type `:wq` to quit.

### Manually

The script expects texts files where each card is on its own line and that terms (the part printed)
and definitions (the part typed/tested) are seperated by a tab. (E.g. `term\tdef\nterm2\tdef2`)

## Run Program

### python

Open you terminal app and run `which python` to determine the location of your installation of
python. Then update the first line in `quizlet.py` to be `#!<output of which python here>` (you can
do this using a program like TextEdit).

### Execute permissions

To navigate to the folder where the program is you will need to run `cd ~/<path>`. For example if
this program is in a folder named `quizlet` in your Downloads folder you will need to run
`cd ~/Downloads/quizlet`. Give the file executable permissions by running: `chmod +x quizlet.py` in
your terminal.

You should now be able to run the program `./quizlet.py path/to/word/list.txt`. For example to use a
word list in my quizlet folder called `french.txt` you would run `./quizlet.py french.txt`.

## Program Features

At the beginning of each run of the program you will be asked how many times you want to review each
term. If you simply hit enter then you will be tested on each term until you correctly type it once.

The program is split into rounds and on each round the words are shuffled. The first N rounds (where
N is the number given at the start of the program) contain of the whole word list. Each round also
contains the words that we gotten wrong in the previous rounds. At the end of each round you will be
presented with the total number of terms that were incorrect in that round.

When you get a term wrong you are given the opportunity to accept it as correct in case of some
small discrepancy (use your judgement). To override the wrong answer you have to type `yes` and hit
enter. Otherwise it will have you retype the word and will add it back to the list for you to try
again.

At the end the program will print out your score (number of terms right / number of terms typed) and
provide you with a list of your missed terms in order of how often they were missed. It will then
prompt you if you want to save these terms to a file. If you hit enter the program will terminate,
however if you answer `y` to this prompt then it will ask for a filename. It will then save all of
your missed terms to that file in the correct format so that you can run the program again on only
the terms missed.
