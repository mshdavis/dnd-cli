import click
import components.roller as roller
import components.str_interpreter as interpreter
import components.character as character


@click.group()
def cli():
    """Entrypoint for dnd cli"""
    pass

@cli.command()
@click.argument('file', type=click.Path(exists=True))
def loadchar(file):
    """
    Method for tellng the cli to reference a character sheet json.
    Pre-requisite for using most of this tool's features.
    Example: 'dnd loadchar ./example-character.json'
    """
    character.load_character(file)
    click.echo('Loaded character file {}'.format(click.format_filename(file)))

@cli.command()
@click.argument('action')
def do(action):
    """
    Method for executing a custom string command defined in a character json under the reserved 'character.actions' section.

    An extension of the raw eval functionality.
    """
    command = character.get_character_value('character.actions.{}'.format(action))
    click.echo('Rolled a {}'.format(interpreter.interpret_command(command)))


@cli.command()
@click.option('--dice_max', '-d', default=20,
              help='Max number on die. I.e 20 for a d20')
@click.option('--num_dice', '-n', default=1,
              help='Number of dice to roll')
def roll(dice_max, num_dice):
    """
    Direct command for rolling dice.
    Example: 'dnd roll -n 2 -d 20'
    """
    click.echo('Rolled a {}'.format(roller.roll(dice_max, num_dice)))

@cli.command()
@click.argument('command')
def eval(command):
    """
    Method for evaluating a text command.
    Will eventually contain support for character sheet variables.
    Example: 'dnd eval "1d6+2".
    """
    click.echo('Rolled a {}'.format(interpreter.interpret_command(command)))
