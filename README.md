# 3aransia

The Latin/Digit Moroccan Language Framework

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![GitHub last commit](https://img.shields.io/github/last-commit/google/skia.svg)

## Prerequisites

- [`Python 3`](https://www.python.org/downloads/)
  
## Installation

```pip install aaransia```

## Usage

```python
from aaransia import transliterate_moroccan, transliterate_moroccan_arabic

s_1 = "ktb bl3rbya hnaya"
s_2 = "كتب بلعربيا هنايا"

print(transliterate_moroccan(s_1))
print(transliterate_moroccan_arabic(s_2))
print(transliterate_moroccan_to_latin(s_1))
print(transliterate_moroccan_arabic_to_latin(s_2))
```

```
>>> كتب بلعربيا هنايا
>>> ktb bl3rbya hnaya
>>> ktb bl'rbya hnaya
>>> ktb bl'rbya hnaya
```

## Other related projects

- [3aransia.api](https://3aransia.github.io/3aransia.api) The api of 3aransia
- [3aransia.web](http://3aransia.com) The web application of 3aransia
