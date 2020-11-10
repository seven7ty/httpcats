# httpcats [![Badge](https://img.shields.io/pypi/v/httpcats?color=3776AB&logo=python&style=for-the-badge)](https://pypi.org/project/httpcats/) [![Badge 2](https://img.shields.io/pypi/dm/httpcats?color=3776AB&logo=python&style=for-the-badge)](https://pypi.org/project/httpcats/)
Getting URLs to your favourite HTTP Cats made easy!


### Installation

Installing `httpcats` is easy, just run `pip install httpcats`!

### Usage

I've developed `httpcats` to make using HTTP Cats simple and fun.

Currently, you can get your cats using one of two functions - `cat_by_name` and `cat_by_code`

`cat_by_name(name: str)` takes in a sole parameter - `name`, which is the status code name to get a cat for.
Upon finding a cat matching the name, it returns an `HTTPCat` object. Here's an example -

```py
from httpcats import cat_by_name

my_cat = cat_by_name("Success")

print(f"My cat has a code of {my_cat.code} and means {my_cat.name}! The URL is {my_cat.url}")
# Prints - 
# My cat has a code of 200 and means Success! The URL is https://http.cat/200
```

`cat_by_code(code: int)` is extremely similar to `cat_by_name`, just using a status code value.
Upon finding a cat matching the code, it returns an `HTTPCat` object. Here's an example -

```py
from httpcats import cat_by_code

my_cat = cat_by_code(404)

print(f"My cat has a code of {my_cat.code} and means {my_cat.name} :( The URL is {my_cat.url}")
# Prints - 
# My cat has a code of 404 and means Not Found :( The URL is https://http.cat/404
```

##### The HTTPCat object also has an `image` attribute

You can use this attribute to get the image bytes associated with the cat.
You can then save it or view it, like in the example below -

```py
from httpcats import cat_by_code
from PIL import Image
from io import BytesIO

my_cat = cat_by_code(302)

cat_image = Image.open(BytesIO(my_cat.image))
cat_image.show()

# Output below -
```

<img src="https://http.cat/302" alt="Cat" width="300"/>

### Contributing 

This package is opensource so anyone with adequate python experience can contribute to this project!

### Report Issues
If you find any error/bug/mistake with the package or in the code feel free to create an issue and report it [here.](https://github.com/itsmewulf/httpcats/issues)

### Fix/Edit Content
If you want to contribute to this package, fork the repository, make your changes and then simply create a Pull Request!

### Contact
If you want to contact me -<br>
**Mail -** ```wulf.developer@gmail.com```<br>
**Discord -** ```wulf#9716```
