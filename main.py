import sys

import click
import six
import yaml
from scss import Compiler


def parse_data(data, indentation_level=0):
    for key in data:
        # Check if this rule has any properties defined.
        if len(data[key]) == 0:
            continue

        print '\n{}{} {{'.format(
            ' ' * (indentation_level * 4),
            key
        )

        indentation_level += 1

        for value in data[key]:
            if isinstance(data[key][value], basestring):
                print '{}{}: {};'.format(
                    ' ' * (indentation_level * 4),
                    value,
                    data[key][value]
                )
            elif isinstance(data[key][value], dict):
                parse_data({value: data[key][value]}, indentation_level)

        indentation_level -= 1

        print '{}}}'.format(
            ' ' * (indentation_level * 4),
        )


@click.command()
@click.argument('infile', type=click.File('rb'))
@click.argument('outfile', type=click.File('w+'))
@click.option('--format', type=click.Choice(['scss', 'css']), default='css')
def main(infile, outfile, format):
    yaml_file = infile.read()
    yaml_data = yaml.load(yaml_file)

    # Cache the current STDOUT, then replace it with a StringIO instance.
    cached_stdout = sys.stdout

    program_output = six.StringIO()
    sys.stdout = program_output

    # This will print to STDOUT, which will be captured into StringIO.
    parse_data(yaml_data)

    program_output.seek(0)
    scss_data = program_output.read()

    if format == 'scss':
        outfile.write(scss_data)
    elif format == 'css':
        outfile.write(Compiler().compile_string(scss_data))

    sys.stdout = cached_stdout


if __name__ == '__main__':
    main()
