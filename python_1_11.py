keys = ['k1', 'k2', 'k3', 'k4', 'k5', 'k6']
values = ['v1', 'v2','v3', 'v4', 'v5','v6', 'v7']

def create_dict(keys, values):
	dict = {}
	for k, v in zip(keys, values):
		dict[k] = v
	return dict

print(create_dict(keys, values))