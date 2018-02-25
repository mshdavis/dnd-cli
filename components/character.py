"""Character sheet interaction."""
import os
import json
import click


def get_character_value(key, cache_data=None):
    """
    Helper method to pull values from character data.
    Params:
        key: A period separated string of keys e.g. 'character.status.health'.
        cache_data: A dict of character data that can be passed in if it's
            already been loaded. If None, this method will load the cache.
    """
    if not cache_data:
        cache_data = load_cache()

    keys = key.split('.')
    character_value = cache_data.get('current_character_data')
    try:
        for k in keys:
            character_value = character_value[k]
    except:
        raise click.ClickException('Error getting value at {}. Please check you character json or your value key.'.format(key))
            
    return character_value


def load_cache():
    """
    Helper method to load cache into memory and handle FileNotFound case.
    """
    cache_data = None
    try:
        with open('./.dnd-cache.json', 'r+') as cache:
            cache_data = json.loads(cache.read())
    except:
        raise click.ClickException('Cache not found. Please load a character file before running commands that rely on one.')

    return cache_data

def load_character(path):
    """
    Helper method that loads a character into the .dnd-cache.json.
    Currently overwrites the cache completely.
    """
    with open(path, 'r') as character_file:
        character_json = json.loads(character_file.read())

    if not character_json:
        raise click.ClickException('File {} could not be parsed as json'.format(path))

    cache_json = {
        'current_character_path': path,
        'current_character_data': character_json
    }

    with open('./.dnd-cache.json', 'w') as cache:
        cache.write(json.dumps(cache_json))
