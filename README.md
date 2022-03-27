# DiceBear PIP CLI
[![Downloads](https://static.pepy.tech/personalized-badge/dicebear?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/dicebear) [![Downloads](https://static.pepy.tech/personalized-badge/dicebear?period=month&units=international_system&left_color=grey&right_color=orange&left_text=Downloads/Month)](https://pepy.tech/project/dicebear) \
[`dicebear`](https://pypi.org/project/dicebear-cli/) is a CLI for https://pypi.org/project/dicebear.
Using this CLI you can get avatars for your program (to get customised avatars use the wrapper instead).
\
For an example go to [`examples/dicebear.sh`](https://github.com/jvherck/dicebear-cli/tree/main/examples).

---

## Useful links
* Dicebear API wrapper: https://pypi.org/project/dicebear/
* Dicebear pip CLI: https://pypi.org/project/dicebear-cli/
* Dicebear API wrapper GitHub: https://github.com/jvherck/dicebear
* Dicebear: https://dicebear.com

---

## How to install
Run `pip install dicebear-cli`\
If that doesn't work try `py -m pip install dicebear-cli`

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
dicebear create avataaars -s John Apple -f svg
```

---

### Styles
All the possible avatar styles. \
https://avatars.dicebear.com/styles

* `adventurer`
* `adventurer-neutral`
* `avataaars`
* `big-ears`
* `big-ears-neutral`
* `big-smile`
* `bottts`
* `croodles`
* `croodles-neutral`
* `identicon`
* `initials`
* `micah`
* `miniavs`
* `open-peeps`
* `personas`
* `pixel-art`
* `pixel-art-neutral`


### Formats 
These are the only supported formats.

* `png`
* `svg`

---

## Credits
Special thanks to [DiceBear](https://github.com/dicebear) 
([Florian Körner](https://github.com/FlorianKoerner)) 
for making this amazing API and to all artists that helped 
making avatars!

## Licenses and privacy policy
- Dicebear **Licenses**: https://avatars.dicebear.com/licenses
- Dicebear **Privacy Policy**: https://avatars.dicebear.com/legal/privacy-policy
- Dicebear Python CLI (this project): https://github.com/jvherck/dicebear/blob/main/LICENSE