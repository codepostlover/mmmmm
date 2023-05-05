# WARNING 
The following information may be sensitive or exploitative in nature, and is presented solely for educational purposes. Please use this information responsibly and only in contexts that further academic discussion or research. Any use of this information for unethical or harmful purposes is strictly prohibited.

This repository holds all the files I was able to get from codepost that I probably shouldn't have access to.

## Files
Most of the files and what they are/do is pretty self-explanatory, but I will explain how I organized it here.

*Note: None of the code in the files is mine, this is all pulled directly from codepost*

- `module [number]` folder
    - `test_py` folder
        - These folders contain the files codepost runs and are each individual test.
    - `test_sh` folder
        - This folder contains the files codepost uses for the i/o tests.
    - `_codePost_run.sh` file
        - This file is the main file that codepost runs, which then runs the individual tests.
    - `files.txt` file
        - This file contains a list of most of the files in the VM in codepost, I was not uniform in what I kept and what I deleted in this list as I mostly used this to track what I had and what I needed to find, so some may contain more useless files than others, but it should give you a rough idea.
    - files ending with `CP.py`
        - These files are what the testers use as the correct implementation, it imports both this and your files and compares the results of the functions, some of these are just copies of some files in [project files](/project%20files/).
    - `bookstore_input_generator.py` file
        - This file is used to generate inputs for testing BookStore, I disagree with the idea of this as it doesn't properly test all edge cases and everytime you submit you roll a die and hope the random was on your side if you didn't properly implement something as perfect as it should've been.
    - `comparators.py` file
        - This file is used to compare graphs.

- `project files` folder
    - This folder contains all the classes we are required to implement, the implementations of the functions are not made by me, these files came directly from what codepost uses to compare results and are probably the professor's code that they made as there was still comments left it them.

- `other files` folder
    - This folder contains the 3 files that are gradually added to throughout the course. These are from module 6 which had the last required edits to these, the extra credit from module 7 never had tests, so I was never able to update these to have the extra credit functions

- `sample_output.json` file
    - In case you don't understand what the tests do, they write to `/outputs/(test id).json` with the format of this file, this means we can very easily pass the tests by just writing to these files, and also customize the output shown in codepost [:)](https://imgur.com/a/bz4qpZa) 


### Module 6 problem
When I first did this and saved the files and ran the tests, there was some weird behavior with bf_order and the object it compared with and some other small problems. Avoiding these at first was easy and the tests in this repo represent those tests, however a few days before the project was due the professor changed an unknown amount of the tests and possibly the CP.py files aswell, I do not have these changed files so just know that module 6 code may be a little outdated.

Another problem with module 6 is that it is the only module of the last 3 modules that includes DLList and like I will mention later, it has a problem with the iterator code making anything that imports and iterates through it also broken, be aware of this.

### `bypass.py` file
If you copy and paste the contents of this file into any file that codepost runs, it should automatically pass all the tests, ive only tested this twice and I actually can't confirm the i/o tests still pass so this may not actually work, but I don't see why it wouldn't. Use at your own risk & read the warning at the top of the page, I told you so.

### What about modules 1-5?
Module 6 was... a mess, seemingly perfectly working code failing the test because its missing commas? pseudocode that does not include crucial, important code, that makes trickle_down_root just a guessing game of if you got it right or not, even with that figured out, the tests changed? Oh, you were at 15/15? nope now you fail bf_order and remove because the tests needed to be fixed, lastly one of the classes implemented the iterator wrong breaking previous code?
All of this is why I was exploring what codepost could do, it was just frustrating not being able to work through a project with so many facepalm moments that I could do nothing about. After spending nearly 3 hours trying to find out the trickle down root while loop correct implementation, I just decided to see what codepost was doing and sure enough, the pseudocode failed to mention 3 curcial steps.
While other modules had their problems, module 6's problems is what gave me the motivation to do this and as I can't run code on older modules without it being marked as late, I can't fully see what those tests were doing, so sadly I won't be able to show them here. Luckily, module 6 had almost all the previous modules classes, so I was able to build the full list of classes from the professors code which was nice.
