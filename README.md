# pyGlue

pyGlue is a Python library for dealing with a glued word. It supports both monolingual and bilingual corpus word ungluing.

## Installation

- Clone this repository

```git
git clone https://github.com/Kawaeee/pyglue.git
```

- Install required packages

```bash
pip install -r requirements.txt
```

## Usage & Example

pyGlue reads input from stdin and writes output to stdout. So, You can adapt pyGlue to any variation as you want.

```bash
# Input
echo -e "LinuxOperating systems such as UNIX only." | python pyGlue.py > mono.out
echo -e "Corgi.ai is an open-source app framework for Corgilover.\tCorgi.ai es un marco de aplicación de código abierto para los amantes de Corgi." | python pyGlue.py > bi.out

# Output
Linux Operating systems such as UNIX only.
Corgi.ai is an open-source app framework for Corgi lover.	Corgi.ai es un marco de aplicación de código abierto para los amantes de Corgi.
```

## To-Do Lists
- Add a custom dictionary to limit aggressive word segmentation