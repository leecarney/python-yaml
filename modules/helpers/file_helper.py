import logging
import ruamel.yaml
import sys
sys.path.append('./ansible/modules')
sys.path.append('../modules')
from os.path import isfile
from typing import (
    Any,
    Dict,
)

# ruamel preserves yaml order
yaml_parser = ruamel.yaml.YAML()


def yaml_to_dict(filename: str) -> Dict[str, Any]:
    data = {}
    if isfile(filename):
        with open(filename) as stream:
            data = yaml_parser.load(stream) or {}

    return dict(data.items())


def load_dict_to_yml_map(yml_data: dict, lookup_key: str) -> str:
    try:
        for key in yml_data:
            if key in {"template_version"}:
                continue

            y_val = yml_data.get(lookup_key)
            if y_val is None:
                logging.getLogger().error(f"Cannot find corresponding value for key {key} in yaml file.")
            else:
                return y_val

    except Exception as e:
        logging.getLogger().error(f"Error loading yaml: {str(e)}", exc_info=True)
