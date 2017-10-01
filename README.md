# Similidrug
## A Python script to automate the calculation of drug name similarty scores for lists of drugs

### Description

Similidrug is a python3 script that uses lingpy ( http://lingpy.org/ ) and optionally strcmp2 ( http://www.cs.toronto.edu/~aditya/strcmp2/ ) to calculate bisim string similarity scores for pairs of strings. The input should be a utf-8 encoded text file with one string per line. The script will compute all possible pairs from the list and return similarity scores using the Bi-Sim algorithm. The results are sorted with more similar pairs at the top, and the top 5000 scores are output to a utf-8 encoded csv file.

The script will accept a maximum of 1000 lines in the input text file, as python limits recursion depth to 1000 levels. However, the code could be modify to compute all possible pairs iteratively instead of recursively to bypass this limit.

### Code Example

Run the script from the command line with the text file as an argument. If strcmp2 is used, the measures.pm and eval.pl files should be placed in the same directory as the computescores.py file.

Example in bash: python3 computescores.py list.txt

If your list is large, and especially if you use the strcmp2 option, consider running the process in the background.

Example in bash: nohup python3 computescores.py list.txt &

The script will be significantly slower when using the strcmp2 scripts because the a call to the perl script eval.pl is made for each pair to evaluate. Future versions of Similidrug should aim to optimize this part of the code.

### Motivation

The aim of the project is to automate the calculation of similarity scores using the bi-sim algorithm to identify look-alike, sound-alike drug name pairs, as described in:

Kondrak G, Dorr B. Automatic identification of confusable drug names. Artificial Intelligence in Medicine 2006; 36(1):29-42; doi: 10.1016/j.artmed.2005.07.005

and

Rash-Foanio C, Galanter W, Bryson M, et al. Automated detection of look-alike/sound-alike medication errors. Am J Health Syst Pharm 2017; 74(7): 521-527; doi: 10.2146/ajhp150690

However, the script can accept any list of strings, not only drug names.

Note that bisim scores calculated using lingpy are inverted as compared to those obtaines using strcmp2. That is, similar strings will score close to 0 when evaluated using lingpy, and close to 1 when evaluated using strcmp2.

### Installation

The script is written for python3. Calculations will require the lingpy python package and all its dependencies. If the strcmp2 is used, obtain the script from the project website listed above, and place the Measures.pm and eval.pl files in the same directory as computescores.py


## Contributors

This script was developed by Maxime Thibault.

## License

Apache v2.0

Copyright 2017 Maxime Thibault

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.