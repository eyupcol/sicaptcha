# Python captcha module (Django/Flask)

## Install
```
pip install sicaptcha
```
## Basic Usage (with default settings)
```
from sicaptcha import sicaptcha as sc

captcha = sc.Sicaptcha()

print(captcha.get_captcha())
# output: base64 coded image
# you can use it in <img src="data:image/webp;base64,output">

```
