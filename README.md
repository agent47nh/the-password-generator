# Password Generator

Generate passwords more easily with complexities!

## Usage

Use it in your scripts like this

```python
from thepasswordgenerator import PasswordGenerator

generator = PasswordGenerator(length=16, upper=2, 
                              lower=2, special=2, numbers=2)
print(generator.generate_password())
```
