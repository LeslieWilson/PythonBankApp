DOCUMENTATION

HOW TO START

PythonBankApp:
run "python3 Bank.py" to run command line programming

SinatraBankApp:
run 'ruby server.rb'
open the website at localhost:4567


First I wrote a banking app in ruby that uses sinatra to throw a view up, and used object oriented programming to build it.

Then I wrote a banking app in Python using ‘procedural’ programming style, as an alternative to using object oriented programming. I'll explain procedural first.

Procedural programming means not assembling your functions wrapped in classes, you just write them separately each as their own thing and write the program ‘top-down’ in this way. It can feel easy to write programs in this way and simple but as your programs get longer using object oriented programming to organize functionality is suggested for the following reasons [(see procedural programming, paragraph two)](https://www.codementor.io/learn-programming/comparing-programming-paradigms-procedural-programming-vs-object-oriented-programming).


Object oriented programming allows for the creation of ‘widgets’ so you can find things more easily and have a sort of stop in the decision tree (modularity) as you are revisiting code. This allows for easier software maintainability- you can more easily alter things and reuse them.

This is opposed to procedural programming which can sometimes feel like it just goes on and on without a break or separation which can lead to confusion in longer programs as you try to revisit them.

OOP is also extensible, meaning you can add new attributes and behaviors to them and make them fit in other places pretty easily. This can, however, also lead to assumptions about how to reuse these objects, because reuse is made easier.

For example, if you have twenty Christmas gifts pre-wrapped and ready to be sent out to relatives, you might send someone the wrong gift more readily than if you needed to view each part in and of itself before figuring out how to send these items out.

Object oriented programs tend to be longer and therefore slower to run than procedural programs, however OOP tends to  cost less to develop because you are able to reuse a lot of code.[See Advantages and Disadvantages of Object-Oriented Programming]( https://resources.saylor.org/wwwresources/archived/site/wp-content/uploads/2013/02/CS101-2.1.2-AdvantagesDisadvantagesOfOOP-FINAL.pdf)


How it was to write this:


After just making sure I was following procedural programming (because I’m mostly familiar with OOP) I realized it’s not that different than what I’d done for my Sinatra app. I first wrote the Sinatra app for the command line using a partly procedural style, so I just re-wrote this part in python when the time came.

Some major differences between the python and Sinatra app was simply the language- I was constantly looking up the correct syntax in python, I’d forgotten a lot of it and forgotten how specific it can be. Eventually I got the hang of it, and the biggest challenge was getting the checking and savings balance to write to a file. So I had to use some resources for that-

I read [this article about Reading and Writing to the same file]( https://stackoverflow.com/questions/14271216/beginner-python-reading-and-writing-to-the-same-file?fbclid=IwAR0QqI0jzWgQ9PQyxH3uHWRlQx2yVeyaBt3zll8ldPI2ESh0NWSUFs483yQ)

I successfully got the file to read, but getting each file to write correctly also took some time.
And I also hit some snags converting strings to integers in this conversion that I had to research.

I hit this error, “AttributeError, :’int’ object has no attribute ‘write’. And [this stackoverflow conversation]( https://stackoverflow.com/questions/23204593/attributeerror-int-object-has-no-attribute-write) showed me that I had overwritten the variable saved as my open file with an integer.

Errors I encountered regarding this, include “ValueError: invalid literal for int() with base 10:”. This happened when the file I was trying to write to, “savings.txt” or “checking.txt” was empty as I tried to change whatever they contained (which was nothing) into an integer. This was solved by starting out my accounts containing a number, but I also could have allowed for that by excepting an error:
try:
   int('')
except ValueError:
   pass      # or whatever

or if you’re not sure that your list is actually a list of stringafied integers or floats you can use something like

n = int(line) if line.is_integer() else int(float(line))


And finally I had to [read about how to use string interpolation]( https://realpython.com/python-string-formatting/) to print the final balance of each account to the command line.


I’ll speak more specifically to my Sinatra app last, because it was an easier endeavor for me. I’m more familiar with ruby and making MVC apps. This was an object-oriented app, that I basically wrote the dialogue for first, then made methods in classes OOP style depending on what the conversation asked for. So I wrote this for the command-line interface first. I pulled down an old Sinatra app template I’d used before and started making routes to make my views, and buttons you click to navigate.

The tricky part of building this was remembering to use the POST method in my form, so the amount of money a user input that they wanted to move, would actually  go through to my text file. As with python, I had to convert whatever was input into an integer but using the to_i method on the params passed through was a lot easier than trying to figure out how to use int(whatever). This again was just a matter of familiarity with the language.

I read about reading and writing to a file with ruby [here]( http://ruby.bastardsbook.com/chapters/io/
