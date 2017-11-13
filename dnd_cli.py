import click
import utils


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
    click.echo('Rolled a {}'.format(utils.roll(dice_max, num_dice)))
