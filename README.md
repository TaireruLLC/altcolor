
# AltColor 

**AltColor** is a Python package designed to add color to text in console-based applications, making it easy to create visually appealing outputs.

---

## Predefined Colors
AltColor provides a variety of predefined colors for your text, some of which are credited to [Colorama](https://pypi.org/project/colorama/). These predefined colors include:

- **Standard Colors**:  
  `BLACK`, `RED`, `GREEN`, `YELLOW`, `BLUE`, `MAGENTA`, `CYAN`, `WHITE`  

- **Light Colors**:  
  `LIGHTBLACK`, `LIGHTRED`, `LIGHTGREEN`, `LIGHTYELLOW`, `LIGHTBLUE`, `LIGHTMAGENTA`, `LIGHTCYAN`, `LIGHTWHITE`  

Additionally, you can define custom RGB colors for even more flexibility!

---

## Installation

Install AltColor via pip:

```bash
pip install altcolor
```

---

## Example Code

```python
from altcolor import colored_text, leaked_text, reset, cPrint

# Use RGB to color your text
print(colored_text((244, 5, 7), "Hello World!"))

# Regular print for comparison
print("Hello World!")

# Use predefined colors
print(colored_text("BLUE", "Hello World!"))

# Leaked text spills into subsequent print statements until reset() is used
print(leaked_text("RED", "Hey,"))
print("you")
print("are" + reset())

# Leaked text can also spill into the background
print(leaked_text("WHITE", "cool!", "Back"))
print("How")
print("are")
print("you?" + reset())

# Use cPrint for controlled or leaked outputs
cPrint(color="RED", text="Hello World!", objective="controlled")
print("Hello World!")
cPrint(color="RED", text="Hello World!", objective="leaked")
print("Hello World!" + reset())
print("Hello World!")
```

---

### Key Features:

1. **Colored Text with RGB**: Use custom RGB values to style your text.
2. **Predefined Colors**: Quickly style text with easy-to-use predefined colors.
3. **Leaked Text**: Color spills into subsequent output until explicitly reset.
4. **Background Color**: Apply color to text backgrounds.
5. **Controlled Printing**: Use `cPrint` for precise and formatted color control.

---

### Links
- **PyPI:** [AltColor on PyPI](https://pypi.org/project/altcolor/)
- **GitHub:** [AltColor Repository](https://github.com/your-repository-url)

---

Happy coding, and bring your console to life with **AltColor**!