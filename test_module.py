# #!/usr/bin/python
import sys
import ruamel.yaml
sys.path.append('../modules/helpers')

yaml_parser = ruamel.yaml.YAML()


def test_get_template_complete():
    template_path = "../modules/TEMPLATE.yml"
    template_data = yaml_parser.load(template_path)

    for key in template_data:
        if key == "template_version":
            continue
        assert key in template_path, f"{key} not in template_path"
