# Simple Calculator CLI

A basic command-line calculator application built in Python that performs fundamental arithmetic operations.

## ðŸ“‹ Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Example Output](#example-output)
- [Known Limitations](#known-limitations)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)

## âœ¨ Features

- **Basic Arithmetic Operations**:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (Ã—)
  - Division (Ã·)
- **Interactive Menu System**
- **Continuous Operation Loop**
- **Simple Exit Functionality**
- **Clean Command-Line Interface**

## ðŸ”§ Requirements

- Python 3.x
- Terminal/Command Prompt
- Any text editor (VS Code, Sublime Text, etc.)

## ðŸ“¦ Installation

1. **Clone or Download**:
   ```bash
   git clone [your-repository-url]
   cd calculator-cli
   ```

2. **No additional dependencies required** - uses only Python standard library

## ðŸš€ Usage

1. **Run the calculator**:
   ```bash
   python calculator.py
   ```

2. **Follow the on-screen prompts**:
   - Select an operation (1-5)
   - Enter your first number
   - Enter your second number
   - View the result
   - Choose to continue or exit

3. **Exit the program**:
   - Select option `5` from the menu

## ðŸ—ï¸ Code Structure

### Functions
```python
def add(a, b)      # Addition operation
def sub(a, b)      # Subtraction operation  
def mul(a, b)      # Multiplication operation
def div(a, b)      # Division operation
```

### Main Program Flow
1. **Display Menu** - Shows available operations
2. **Get User Choice** - Accepts operation selection (1-5)
3. **Handle Exit** - Terminates program if option 5 is selected
4. **Get Numbers** - Prompts for two integers
5. **Perform Calculation** - Executes selected operation
6. **Display Result** - Shows formatted output
7. **Loop** - Returns to menu for next operation

## ðŸ“ Example Output

```
========================================
Choose from 1 to 4 
========================================
1. Add
2. subtract
3. Multiply
4. Divide
5. Exit
plsease select option between 1 to 4 :1
Enter 1st number (only number) 15
Enter 2nd number (only number) 25
15 + 25 = 40

========================================
Choose from 1 to 4 
========================================
1. Add
2. subtract
3. Multiply
4. Divide
5. Exit
plsease select option between 1 to 4 :4
Enter 1st number (only number) 20
Enter 2nd number (only number) 4
20 / 4 = 5.0

========================================
Choose from 1 to 4 
========================================
1. Add
2. subtract
3. Multiply
4. Divide
5. Exit
plsease select option between 1 to 4 :5

Thank you for using the calculator!
Goodbye! ðŸ‘‹
```

## âš ï¸ Known Limitations

1. **Integer Input Only**: Currently accepts only integer inputs
2. **No Error Handling**: 
   - Division by zero will cause a runtime error
   - Non-numeric inputs will crash the program
3. **Limited Validation**: No input validation for menu choices
4. **Basic UI**: Simple text-based interface

## ðŸ”® Future Improvements

- [ ] Add error handling for division by zero
- [ ] Support for decimal/floating-point numbers
- [ ] Input validation for all user inputs
- [ ] More advanced operations (power, square root, etc.)
- [ ] History of calculations
- [ ] Better error messages
- [ ] Unit tests
- [ ] GUI version

## ðŸ“ File Structure

```
calculator-cli/
â”œâ”€â”€ calculator.py    # Main calculator script
â”œâ”€â”€ README.md       # This documentation
â””â”€â”€ .gitignore      # Git ignore file (optional)
```

## ðŸ¤ Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add some improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## ðŸ“œ License

This project is open source and available under the [MIT License](LICENSE).

## ðŸ‘¨â€ðŸ’» Author

**Ranjan** - Python Developer Internship Task

## ðŸŽ¯ Learning Objectives Achieved

- âœ… **Functions**: Implemented separate functions for each operation
- âœ… **Loops**: Used `while True` loop for continuous operation
- âœ… **Conditionals**: Applied if-elif-else statements for menu logic
- âœ… **CLI Interaction**: Created interactive command-line interface
- âœ… **User Input**: Utilized `input()` function for user interaction

---

*This calculator was created as part of a Python Developer Internship task focusing on fundamental programming concepts.*