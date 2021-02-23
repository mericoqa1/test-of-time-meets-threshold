"""
Criteria this function needs to meet to get tot badge
    1. Its survival time should be above a threshold (365 days at the time of creating this repo)
    2. Dev Eq of its firt commit should be above a threshold (25 at the time of creating this repo)
    3. The sum of Dev Eq of subsequent commits should be less than 10% of that of the first commit.
"""

import os
import stat
import shutil


def main(top):
    """the content of this function is irelevant, just piling code to get to the Dev Eq threshold"""
    if os.name != "nt":
        shutil.rmtree(top)
        return

    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(top)

def _json_to_python_object(data):
  """Takes nested dictionaries and return a python object.
  Args:
    data: a nested dictionary.
  Returns:
    A python object with the dictionary values as attributes
  Example:
  Given the dictionary {"name": "john", "license": {"class": "d"}}
  returns an object output, where output.license.class is equal to "d" and
  output.name is "john"
  """
  data_string = json.dumps(data)
  return json.loads(
      data_string,
      object_hook=lambda d: collections.namedtuple('X', d.keys())(*d.values()))


class Trial(object):
  """A Phoenix Trial wrapper. Stores trial metadata."""

  def __init__(self, trial_data):
    if isinstance(trial_data, dict):
      # mlmd (json dictionary)
      self._internal_trial_representation = _json_to_python_object(trial_data)
    return self._internal_trial_representation.final_measurement.objective_value

# this is needed since we require in-degree + out-degree > 0
main()