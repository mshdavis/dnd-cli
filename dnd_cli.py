import click
import components.roller as roller
import components.str_interpreter as interpreter


@click.group()
def cli():
    """Entrypoint for dnd cli"""
    pass


@cli.command()
@click.option('--dice_max', '-d', default=20,
              help='Max number on die. I.e 20 for a d20')
@click.option('--num_dice', '-n', default=1,
              help='Number of dice to roll')
def roll(dice_max, num_dice):
    """Direct command for rolling dice"""
    click.echo('Rolled a {}'.format(roller.roll(dice_max, num_dice)))

@cli.command()
@click.option('--command', '-c',
              help='Text command to evaluate (i.e. 1d6+2)')
def eval(command):
    """
    Method for evaluating a text command i.e. 1d6+4

    Will eventually contain support for character sheet variables.
    """
    click.echo('Rolled a {}'.format(interpreter.interpret_command(command)))

