Scope Question
==============

In programming languages, variables need to be defined before you can use them.  These variables can be accessed in different ways- globally or locally. So globally and locally scoped variables just denote to what extent within the code that a variable can be accessed.
Variables are containers for objects in memory. Several variables can be mapped to the same instance in some languages. So you can access the objects by the name you choose to assign to them.

If you define a variable at the top of your python script , it will be a global variable, which means it's accessible from anywhere in your script, including from within functions. here is an example of leslie being defined globally

Leslie_age = 33

Def function():
Leslie_age = 20
Print(leslie)

Function()

You can also see that leslie is being defined locally (from within the function) as 20. If you print leslie outside of the function, its globally defined value will be printed. if you print it from inside of the function, its local value will be printed.


So if I wanted to make a function that changes my age, I’d need to use the word ‘global’ in front of the variable, for it to apply to what is inside of the function and allow the function to work. For example:

Leslie_age = 33

Def change_age(new_age):
Global Leslie_age
Leslie_age = new_age

Print(Leslie_age)

Change_age(44)
Print (Leslie_age)

Referenced: [Datacamp](https://www.datacamp.com/community/tutorials/scope-of-variables-python?fbclid=IwAR0Y4cTAF8YECNceK5KN7qj_f_PTGAS0sXdQ-G0FrJUOfmzP6Gzja8k0hB4)

As another example, if I’m inside my car and I want to reach something in the passenger-side seat, my scope is the extent to which I can reach that item on my seat. If I want to apply my grasp to things globally rather than locally, I’d use one of those pincer arms and extend my reach.
So there are several symbols and keywords used by different coding languages that act like this pincer tool, to extend reach.

We talked about what python uses to extend its reach for variables- using the global keyword. And we talked about global and local variables in python. JavaScript also has global and local variables[referred to this article]( https://cs.marlboro.college/courses/fall2016/python/code/functions/ants.py). The definitions for scope are the same in JavaScript as in python. A variable is in the global scope when its defined outside of a function, and local variables are defined inside functions. Also, in JavaScript anything defined in curly braces is defining a new local scope for variables declared with let.

As a comparison, if you put a variable outside a function in python, you can access it in the function but you can’t re-define it globally without labeling it global.

If you put a variable outside of a function in JavaScript you can redefine it in a function or anywhere else you want.  If you assign a variable inside a function with let or var, its only accessible in that function.  If you assign a variable inside curly brackets with let or const, it is only accessible inside that block.  Variables declared with Var ignore curly brackets.

So to summarize the differences between let, const and var- functions create a new scope for variables declared with var, let and const, curly braces usually after if statement or loops make new scope for let and const but not var.

So, to bring in a third language, (and the one that makes the most sense to me) Lets talk about ruby scope. Lets say I have this in python:

Leslie = 33
Def blah():
Print Leslie

Blah() --> this prints 33

Now in ruby:

Leslie = 33
Def blah
Puts Leslie
End

Blah --> throws NameError


So, in ruby when you define a lower case variable its always local, and its only accessible in the block where it was defined.
[referenced]( https://stackoverflow.com/questions/15042691/scope-in-ruby-and-python?fbclid=IwAR1g_RkkaFkVkUoexLcgDP5n_DWdPYcwp7kLc6sqqleE3p8znZSD0jHu6CQ). In ruby for a variable to cross over to other scopes it needs to be something called an ‘instance variable’, which uses a single @variable. This make sit accessible from within the object and from outside with a ‘getter’. There’s also constants, which are variables that start with capitol letters, and are always accessible.  Or it could be a class variable, with double @@variable, which is accessible from within the object or class that defined it and in any subclasses but not from outside of it.
Finally you can have a global variable using a dollarsign $variable which goes across all scopes and is dangerous to use because it doesn’t follow the ‘restricted use principle. This principle applies to all coding languages when it comes to scope, and just says that using scope creates a healthy space between bugs and how much of your code they can effect by making a separation of variable values throughout your code.



My thoughts on python, ruby and javascript:
==========================================

I don’t have a lot of experience with coding and what experience I do have is heavily leaning towards ruby, so I’ll talk about that first, and in comparison to python which is my second most in terms of experience.

I guess supposing you want to build an application as quickly as possible, with as little experience as possible, ruby is the way to go. Ruby is far less nitpicky than python is syntactically. You don’t need colons after you start code blocks in ruby. You don’t need to look out for indentation in ruby. You don’t need to end things in python, but I actually like the clear ending ruby gives you (except for when your code is riddled with end statements and you’re not sure if you’re short one or have an extra three).


if leslie == “tired”
print “of course”
else
print “you’re lying’
end

Vs

if leslie == “tired”:
     print “of course”
else:
     print “duh”


But on the other hand, let’s talk about why you might like some of these nitpicky things about python. I like that it forces me to indent, my code written in ruby tends to look sloppy and it’s hard to keep track of things because nothing is forcing me to. I think end statements are redundant, on the other hand, and it’s kind of a waste of time as you become more experienced in this to mark the end of what clearly has ended. Python supports object oriented programming just like ruby does, and also functional programming. It seems like you can use libraries like Numpy for working with arrays, Pandas for time series data, and Matplotlib for mathematical visualizations. That is it has the support of huge communities and has a lot of really great languages for dealing with data science. The only competitor to python in that regard would be R. [referenced here:](https://news.efinancialcareers.com/uk-en/329153/is-python-best-for-data-science)

But, then again, lets go back to ruby and why it’s so awesome, and actually compare it to the evil java as an example.

Here’s hello world in java:
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, world");
    }
}
And here’s the single line of code that achieves the same thing when written in ruby!

Puts “hello world!”

So you can write less code than you might in some languages.  And that’s still simpler than
console.log(“hello world!”) that you’d find in javascript… But not by much.
Ruby is great for handling complex tasks like making the back end of websites with very readable code.  Javascript is great for designing interactive web front-ends. It’s the only language that runs in the browser and there are some very cool frameworks like react for creating dynamic web-pages.  All of the methods you use in ruby are available in javascript it just feels a little more clumsy.

I also want to mention in regards to ruby that there is some rumor that it is a dying language. But that’s not true. Rails has like 3500 contributors on github as opposed to django, a framework for python, which has about half that number.  Community plays a huge part in determining the popularity and use of a language and the regular contributions of the ruby and rails community are telling.

So in summary, ruby is best used to make websites quickly and has a lot of support for doing this. Python is probably best used for data science because of all the libraries it has for this. Both languages are high-level languages though and are pretty similar in a lot of ways.
Javascript is powerful and runs right from the browser, and I suppose it makes it easy to just get out there and ‘make the thing’ rather than focusing on learning to code.
All of these are pretty good options in terms of learning a language, but I'm pretty done with this exam and am going to go eat pie.  
