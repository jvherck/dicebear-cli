# DiceBear PIP CLI
![Downloads](https://static.pepy.tech/badge/dicebear-cli)
![PyPI](https://img.shields.io/pypi/v/dicebear-cli)
![GitHub issues](https://img.shields.io/github/issues/jvherck/dicebear-cli)
![GitHub](https://img.shields.io/github/license/jvherck/dicebear-cli)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dicebear-cli)
![Maintenance](https://img.shields.io/maintenance/yes/2024)
\
[`dicebear-cli`](https://pypi.org/project/dicebear-cli/) is a CLI for https://pypi.org/project/dicebear.
Using this CLI you can get avatars for your program (to get customised avatars use the wrapper instead).
\
For an example go to [`examples/dicebear.sh`](https://github.com/jvherck/dicebear-cli/tree/main/examples).


---


## Useful links
* Dicebear pip CLI: https://pypi.org/project/dicebear-cli/
* Dicebear API wrapper: https://pypi.org/project/dicebear/
* Dicebear API wrapper GitHub: https://github.com/jvherck/dicebear
* Dicebear: https://dicebear.com


---


## How to install
Run `pip install dicebear-cli` \
If that doesn't work try `python -m pip install dicebear-cli`


---


## Usage
It can quickly create one or more avatars at a time but it can't take options.

```shell
dicebear --help
```
```shell
dicebear create --help
```
```shell
dicebear create avataaars -s "John Apple" -f svg
```


---


### Styles  
All the possible avatar styles. \
https://dicebear.com/styles  
  
* `adventurer`  
* `adventurer-neutral`  
* `avataaars`  
* `avataaars-neutral`  
* `big-ears`  
* `big-ears-neutral`  
* `big-smile`  
* `bottts`  
* `bottts-neutral`  
* `croodles`  
* `croodles-neutral`  
* `fun-emoji`  
* `icons`  
* `identicon`  
* `initials`  
* `lorelei`  
* `lorelei-neutral`  
* `micah`  
* `miniavs`  
* `notionists`
* `notionists-neutral`
* `open-peeps`  
* `personas`  
* `pixel-art`  
* `pixel-art-neutral`
* `rings`
* `shapes`
* `thumbs`


### Formats   
These are the only supported formats.

* `DFormat.svg` (default)  
* `DFormat.png`  
* `DFormat.jpg`  
* `DFormat.json`  


---


## Credits  
Special thanks to [DiceBear](https://github.com/dicebear) ([Florian Körner](https://github.com/FlorianKoerner)) for 
making this amazing API and to [all artists](https://dicebear.com/licenses) for creating these avatars!  


## Licenses and privacy policy  
- Dicebear **Licenses**: https://dicebear.com/licenses  
- Dicebear **Privacy Policy**: https://dicebear.com/legal/privacy-policy  
- Dicebear Python API wrapper (this project): https://dicebear.vhjan.me/license