from ansible.module_utils.basic import AnsibleModule
import sys
sys.path.append('../modules/helpers')

import file_helper as fh
from typing import (
    Any,
    Dict,
)


def main():
    module = AnsibleModule(
        argument_spec=dict(
            local_filename=dict(required=True, type='str'),
            lookup_yaml_key=dict(required=True, type='str'),
        ),
        supports_check_mode=True
    )

    result = load_yaml_config(
                  module.params["local_filename"],
                  module.params["lookup_yaml_key"],
              )
    module.exit_json(changed=False, data=result)


def load_yaml_config(yaml_filename: str, yaml_key:str) -> Dict[str, Any]:
    out_dict = fh.yaml_to_dict(yaml_filename)
    return fh.load_dict_to_yml_map(out_dict, yaml_key)


if __name__ == '__main__':
    main()
