"""Internal helper module."""
import random


def roll(dice_max=20, num_dice=1):
    """
    Helper method to roll a d{dice_max} die {num_dice} times
    """
    result = 0
    for x in range(num_dice):
        result += random.randint(1, dice_max)
    return result


def roll_multiple(dice_max, num_dice, num_rolls=1):
    """
    Helper method to make a roll multiple times
    """
    results = []
    for x in range(num_rolls):
        results.append(roll(dice_max, num_dice))
    return results


def roll_min_from_multiple(dice_max, num_dice, num_rolls):
    """
    Helper method to roll minimum value from series.
    I.e. disadvantage in 5e
    """
    return min(roll_multiple(dice_max, num_dice, num_rolls))


def roll_max_from_multiple(dice_max, num_dice, num_rolls):
    """
    Helper method to roll maximum value from series.
    I.e. advantage in 5e
    """
    return max(roll_multiple(dice_max, num_dice, num_rolls))
