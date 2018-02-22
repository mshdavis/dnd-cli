"""String command interpretation"""
import re
import click
import components.roller as roller

def interpret_command(command_string):
    dice_pattern = re.compile(r"((^\s?|\s+)\d+d\d+(\s+|\s?))")
    dice_matches = dice_pattern.findall(command_string)
    
    eval_string = ""
    for match in dice_matches:
        roll = handle_dice_roll(match[0])
        eval_string = command_string.replace(match[0], str(roll))

    eval_check = re.compile(r"^[0-9_\s+/*-]+$")
    can_eval = eval_check.match(eval_string)
    if not can_eval:
        raise click.ClickException("Command '{}' could not be parsed. Reduced to '{}' before error.".format(command_string, eval_string))

    return eval(eval_string)

def handle_dice_roll(dice_command):
    params = dice_command.split('d')
    return roller.roll(int(params[1]), int(params[0]))

# TODO: Implement method
def handle_character_ref():
    pass