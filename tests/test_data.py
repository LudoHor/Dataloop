import pytest
from project.dataloop_exercise import Data


def test_data_class():
    # Data for testing
    data = {
        "id": "1",
        "name": "first",
        "metadata": {
            "system": {
                "size": 10.7
            },
            "user": {
                "batch": 10
            }
        }
    }

    # Load from dict
    my_inst_1 = Data.from_dict(data)
    assert my_inst_1.size == 10.7, "Size should be 10.7"

    # Load from inputs
    my_inst_2 = Data(name="my")
    assert my_inst_2.name == "my", "Name should be 'my'"

    # Check default height
    assert my_inst_1.height == 100, "Default height should be 100"
    assert my_inst_1.to_dict()[
        'metadata']['system']['height'] == 100, "Height in dict representation should be 100"
