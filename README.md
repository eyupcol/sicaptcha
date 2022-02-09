# Python captcha module (Django/Flask)


![An example captcha image](https://raw.githubusercontent.com/siteisleri/sicaptcha/master/example.webp)

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
## All settings
```
captcha = sc.Sicaptcha()

captcha.format = 'buffer' # you can use base64, buffer or image
captcha.font = 'arial.ttf' #path to your font
captcha.bgcolor = (255, 255, 255, 255)
captcha.textcolor = (0, 0, 0, 250)
captcha.linecolor = (0, 0, 0, 90)
captcha.fontSize = 48
captcha.imagepath = 'captcha.webp'
captcha.text = '' # text to be used for confirmation
```


## Usage in Django
```
from sicaptcha import sicaptcha as sc

def captcha(request):
    captcha = sc.Sicaptcha()
    captcha.format = 'buffer'
    captcha.font = "pathtoyourfont.ttf"
    output = captcha.get_captcha()
    request.session['captcha_text'] = captcha.text
    return HttpResponse(output, content_type='image/webp')
```
