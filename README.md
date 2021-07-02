# Python captcha module (Django/Flask)


examples: [Siteisleri.com](http://www.siteisleri.com)

## Install
```
pip install sicaptcha
```
## Basic Usage (with default settings)
```
from sicaptcha import sicaptcha as sc

captcha = sc.Sicaptcha()

#you can get the text that visitors will have to submit to confirm they are not a bot
text = captcha.text
output = captcha.get_captcha()
# output: base64 coded image
# you can use it in <img src="data:image/webp;base64,output">
```
