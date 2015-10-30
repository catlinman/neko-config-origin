
/* -------------------------------------------------------------------------------------

This file was initially created for a friend in mind who was working with ActionScript
at the time and really needed a quick rundown of programming in general for a course at
his school. I tried to explain things as easily and simple as possible for him to understand
starting with the pure basics. Thought this might also come in hand for others that barely
have any understanding of code. This right here is ActionScript as you might tell but other
than that it should be easily translatable to any other given programming language. The only
difference here is me using the trace function where as in most other languages it would be
something along the lines of print. Anyway, maybe you can find use in this Cheat sheet.

- Codeflow
	Code runs from the top down line for line. It executes commands from left to right.

- Variables
	Variables store important information that is to be used later on. If for instance the
	program were to calculate a large number and then want to work with it after doing another
	task first, it would be important to save that value to a variable. Variables can have any
	name possible and even include numbers in their definitions. This depends on the language
	though. However, it is important to note that variables do not overwrite already defined
	objects. The name in this case is a sort of space reserved for data. If we overwrite the
	space with new data the old will be lost and can not (well you can but that's not relevant)
	recovered. As with all languages there are certain "spaces" that are already defined and
	will not work if overwritten (you can overwrite them but only if you know what you are doing).

- Datatypes
	Programming languages contain so called types or datatypes. These represent sets of data
	grouped together in a nice way that everyone can understand what they do. Variables are
	declared for instance with a datatype bound to them. Most languages common datatypes
	that appear in a lot of situation. The first are strings which can be seen as a collection
	of characters. A string is usually defined with quotes or double quotes (example: "Word").
	This is required since names without quotes or anything added to them will always count as
	references to variables, functions and all sorts of other base programming things. If for
	instance the user wanted to use the variable called foo he would just write it out like
	that. To receive the actual text foo he would have to reference it in double quotes: "foo".
	Most languages that are strictly typed require you to specify what datatype a variable has
	when you define it. In ActionScript this is done by adding a colon after the variable and
	then writing the type of data that variable is supposed to store (example: coolnumber:Number).

- Functions
	Functions can be seen as user commands. When a function is called by writing the function
	name and then the curved brackets (example: name() ) what it does is it tells the program
	to go to the line of the function name in the file and execute (e.g. run) everything inside
	the curly (example: {} ) brackets. Everything inside of a function remains in the function
	UNLESS it was defined before the actual function itself. In that case a reference to the
	given object is all that is needed to interact with it.
	
	Many languages such as ActionScript (Flash) have built-in functions that you can execute.
	An example of these would be the trace function. This function when called with trace()
	will take in an optional amount of arguments separated by commas. These arguments are
	then passed to your current environment's console. In other languages this is referred to
	as printing or simple output. An example for this would be: trace(1) which would output
	the number 1 to your current console.

	Since everything declared in a function remains within it, the only outside connection is
	achieved through the so called return. A return is usually done at the end of a function.
	What it does is it allows the function to hand back certain values to the user. The same
	as the user hands certain values (arguments/parameters) to a given function, the function
	is able to hand values back to the user. The syntax for this is usually the return command
	followed by a set of variables. This depends on the language in question though.

   ------------------------------------------------------------------------------------- */

// This is a simple loosely typed variable that we can use later on.
// Assignment is done with the equals sign. The var command is used to register a new variable.
var coolnumber = 1;

// If we were to strictly type it we would have to say that coolnumber has the type of Number.
var coolnumber:Number = 1;

// Objects are a special kind of type that contain additional variables and functions.
// They are also created using the 'new' command. 
var coolbutton = new Button(); 

// Once again this can also be strictly typed.
var coolbutton:Button = new Button();

// The properties of objects can be accessed using a dot at the end of the variable's name.
// Note here that 'coolbutton' is already defined and we don't use the var command.
coolbutton.x = 1;

// An object's functions (which are called methods) can be accessed like any other function.
coolbutton.doStuff();

/* ------------------------------------------------------------------------------------- */

// This is a simple function without arguments.
function addition() {
	trace(1 + 2);
}

addition(); // Traces 3 because 1 + 2 -> 3.

/* ------------------------------------------------------------------------------------- */

// This function contains variables that are only accessible inside of the function.
function addition() {
	var a = 1;
	var b = 2;
	trace(a + b);
}

trace(a); // Either traces Undefined or creates an error since a and b only exist in the function.
addition(); // Traces 3 because a + b -> 3.

/* ------------------------------------------------------------------------------------- */

function addition(a, b) {
	trace(a + b);
}

addition(); // Causes an error because a and b do not exist.
addition(1, 2); // Traces 3 because a=1 + b=2 -> 3.

/* ------------------------------------------------------------------------------------- */

var n = 1.4; // We can also define variables outside of functions.
function addition(a, b) {
	trace(a + b + n); // And use these inside of the functions.
}

addition(1, 2); // Traces 4.4 because a=1 + b=2 + n=1.4 -> 4.4.

/* ------------------------------------------------------------------------------------- */

var n = 1.4;
function addition(a) {
	n = n + a; // Variables on the outside can be changed by a function and will remain.
	trace(n);
}

addition(3); // Traces 4.4 because n=1.4 + a=3 -> 4.4.
addition(1); // Traces 5.4 because n=4.4 + a=1 -> 5.4.

/* ------------------------------------------------------------------------------------- */

function addition(a, b) {
	return a + b // The return command sends back variables to the user.
}

var n = addition(1, 2); // We can store the returned value from the addition function in a variable.
trace(n); // Traces 3 because a=1 + b=2 -> 3. This value is then stored in the variable 'n'.

/* ------------------------------------------------------------------------------------- */