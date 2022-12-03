from deepdiff import DeepDiff


d1 = {'status': '0'}
d2 = {'status': '2'}


# {'type_changes': {"root['status']": {'old_type': <class 'str'>, 'new_type': <class 'int'>, 'old_value': '0', 'new_value': 0}}}
# {'values_changed': {"root['status']": {'new_value': '2', 'old_value': '0'}}}
print(DeepDiff(d1, d2))