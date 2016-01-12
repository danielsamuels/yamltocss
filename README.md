# YAML to (S)CSS

The converter that no-one requested, wanted or needed. Converts a YAML file to either SCSS or CSS (default is CSS). Examples can be found in the `examples/` directory.

## Installation

* Clone this project (no, it's not pip installable..)
* `pip install -r requirements.txt`

## Usage

```
Usage: main.py [OPTIONS] INFILE OUTFILE

Options:
  --format [scss|css]
  --help               Show this message and exit.
```

Example: 
```
python main.py input.yaml output.css
```
