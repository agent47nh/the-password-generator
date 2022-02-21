# Password Generator

Generate passwords more easily with complexities!

## Installation

Simply run the following on your command line,

```bash
$ python3 -m pip install thepasswordgenerator
Collecting thepasswordgenerator
  Downloading thepasswordgenerator-1.0.0-py3-none-any.whl (14 kB)
Installing collected packages: thepasswordgenerator
Successfully installed thepasswordgenerator-1.0.0
```

If you are not able to install using pip, you can download the latest package from `https://github.com/agent47nh/the-password-generator/releases` or [click here](https://github.com/agent47nh/the-password-generator/releases) and install it manually.

`$ python3 -m pip install thepasswordgenerator-<version>-py3-none-any.whl`

## Usage

Use it in your scripts like this

```python
from thepasswordgenerator import PasswordGenerator

generator = PasswordGenerator(length=16, upper=2, 
                              lower=2, special=2, numbers=2)
print(generator.generate_password())
print(generator.generate_multiple_passwords(15))
```
