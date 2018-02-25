"""String command interpretation"""
import re
import click
import components.roller as roller
import components.character as character

def interpret_command(command_string):
    """
    Parses command_string and replaces any dice roll commands or
    character references with numbers before evaluating the 
    entire expression.
    """
    cache_data = character.load_cache()

    # Handle dice commands
    dice_pattern = re.compile(r"((^\s?|\s+)\d+d\d+(\s+|\s?))")
    dice_matches = dice_pattern.findall(command_string)
    
    eval_string = ""
    for match in dice_matches:
        roll = handle_dice_roll(match[0])
        eval_string = command_string.replace(match[0], str(roll))

    # Handle character references
    ref_pattern = re.compile(r"({[\w.-]+})")
    ref_matches = ref_pattern.findall(command_string)
    for match in ref_matches:
        ref = handle_character_ref(match, cache_data)
        eval_string = eval_string.replace(match, str(ref))

    # Confirm command can now be evaluated
    eval_check = re.compile(r"^[0-9_\s+/*-]+$")
    can_eval = eval_check.match(eval_string)
    if not can_eval:
        raise click.ClickException("Command '{}' could not be parsed. Reduced to '{}' before error.".format(command_string, eval_string))

    return eval(eval_string)

def handle_dice_roll(dice_command):
    """
    Helper method to replace string dice roll commands with a result.
    """
    params = dice_command.split('d')
    return roller.roll(int(params[1]), int(params[0]))

def handle_character_ref(ref_command, cache_data=None):
    if not cache_data:
        cache_data = character.load_cache()

    ref_command = ref_command.strip('{}')
    return character.get_character_value(ref_command, cache_data)