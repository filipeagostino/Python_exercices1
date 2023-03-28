keys = ['k1', 'k2', 'k3', 'k4', 'k5', 'k6', 'k7']
values = ['v1', 'v2','v3', 'v4', 'v5','v6']

def create_dict2(keys, values):
	dict = {}
	for i in keys:
		dict['keys'] = keys
		dict['values'] = values
	return dict

print(create_dict2(keys, values))