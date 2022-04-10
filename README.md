# pymorse
Python based Morse Code Translator

Translate between morse code and the English language


## Setup
1.) Download this repository, or clone it by
```git clone https://github.com/JacobChesslo/pymorse.git```

2.) Navigate to this project:
```cd <path-to-this-download>```
  
3.) Install it as a package:
```pip install .``` or ```python -m setup install .```

## Use
To import and use pymorse:

```
  import pymorse
  
  
  text = 'Hello World'
  morse_code = pymorse.to_morse(text)
  print("This is Morse Code of Hello World:", text)
  
  code = .... . .-.. .-.. ---   .-- --- .-. .-.. -..
  new_text = pymorse.to_english(code)
  print("This is the Conversion back:", new_text)
  
  titled_text = pymorse.to_english(code, title=True)
  print("This is the Titled Conversion back:", titled_text)
```

Output:

```
  > This is Morse Code of Hello World: .... . .-.. .-.. ---   .-- --- .-. .-.. -..
  > This is the Conversion back: HELLO WORLD
  > This is the Titled Conversion back: Hello World
```
