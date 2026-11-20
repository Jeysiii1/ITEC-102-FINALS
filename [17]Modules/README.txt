A Python module is a file or library that contains code, functions, and tools that we can use in a program.

Modules help us add features to our programs without writing everything ourselves. They make coding easier, more organized, and more efficient.

This folder documents the three Python modules used in the Student Grade Calculator:

1. Math
2. Datetime
3. String

1. MATH MODULE

Purpose:

Math is a built-in Python module used for mathematical calculations. It provides different functions that help us perform mathematical operations easily.

How it is used in the Student Grade Calculator:

The Math module calculates the square root of the student's average grade. It uses the `math.sqrt()` function to get the square root of a given number.

Code:

```
import mathaverage = 90square_root = math.sqrt(average)print("Square Root:", round(square_root, 2))
```

Explanation:

- `import math` loads the Math module into the program.
- `math.sqrt()` calculates the square root of a number.
- `average` stores the student's average grade.
- `square_root` stores the calculated square root.
- `round(square_root, 2)` rounds the result to two decimal places.

Example:

If the student's average grade is 90, the square root will be approximately 9.49.

Other uses:

The Math module can also calculate powers, factorials, absolute values, and other mathematical operations using functions such as `math.pow()`, `math.factorial()`, and `math.fabs()`.

Installation:

No installation is needed. The Math module is included with Python.

2. DATETIME MODULE

Purpose:

Datetime is a built-in Python module used for working with dates and time. It allows programs to get, display, and manage the current date and time.

How it is used in the Student Grade Calculator:

The Datetime module gets the current date from the computer and displays it in the Student Grade Report. This allows the program to automatically show the date when the report is generated.

Code:

```
import datetimetoday = datetime.date.today()print("Date:", today)
```

Explanation:

- `import datetime` loads the Datetime module into the program.
- `datetime.date.today()` gets the current date from the computer.
- `today` stores the current date.
- `print()` displays the date on the screen.

Example:

If the program is executed on November 20, 2026, it will display:

```
Date: 2026-11-20
```

Other uses:

The Datetime module can also display the current time, calculate the difference between two dates, format dates, and work with specific days, months, and years.

Installation:

No installation is needed. The Datetime module is included with Python.

3. STRING MODULE

Purpose:

String is a built-in Python module used for working with text and characters. It provides different tools and predefined character sets that can be used in a program.

How it is used in the Student Grade Calculator:

The String module displays all uppercase letters from A to Z using `string.ascii_uppercase`. This demonstrates how Python can access and display a complete set of alphabetic characters.

Code:

```
import stringletters = string.ascii_uppercaseprint("Alphabet:", letters)
```

Explanation:

- `import string` loads the String module into the program.
- `string.ascii_uppercase` provides all uppercase English letters from A to Z.
- `letters` stores the uppercase alphabet.
- `print()` displays all the letters on the screen.

Example:

The program will display:

```
Alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

Other uses:

The String module can also provide lowercase letters using `string.ascii_lowercase`, numbers using `string.digits`, and punctuation marks using `string.punctuation`.

Installation:

No installation is needed. The String module is included with Python.

------------
 SUMMARY
------------
The Student Grade Calculator uses three built-in Python modules, and each module has its own purpose.


Math - Calculates the square root of the student's average grade. 
Datetime - Gets and displays the current date.                        
String - Provides uppercase letters from A to Z.                   
