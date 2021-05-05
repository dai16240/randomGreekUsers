# Import modules
import random
import dataset
import unidecode

# Connect to sqlite database
db = dataset.connect('sqlite:///data.sqlite')

def generate_place():
	"""
	Generates random location with matching postal code.
	"""
	while True:
		try:
			tk_street_index = random.randint(1, 51595)
			tk_street = db['streets'].find_one(id=tk_street_index)

			street_name = tk_street['street_name']
			tk = tk_street['postal_code']

			region = random.choice([item['region'] for item in db['postal_codes'].find(postal_code=tk)])

			street_no = random.randint(1, 200)
			address = f"{street_name} {street_no}"
			phone_code = db['phone_codes'].find_one(region=region)['phone_code']
			break
		except:
			pass

	return address, tk, region, phone_code


def generate_email(fullname):
	"""
	Returns an email address based on user's full name.
	"""
	first, last = fullname
	first_eng = unidecode.unidecode(first).lower()
	last_eng = unidecode.unidecode(last).lower()
	three_digit = random.randint(1, 999)
	providers = [
		'hotmail.com', 'gmail.com', 'yahoo.com', 
		'yahoo.gr', 'outlook.com.gr', 'outlook.com',
		'otenet.gr', 'gmail.com', 'gmail.com', 'live.com'
	]
	provider = random.choice(providers)
	first_part = first_eng[:random.randint(1, len(first))]
	last_part = last_eng[:random.randint(1, len(last))]
	numeric = random.choice(['', three_digit])
	dot_dash = random.choice(['', '.', '_'])

	return f"{first_part}{dot_dash}{last_part}{numeric}@{provider}"

def generate_cellphone():
	"""
	Returns a 10-digit greek cell number.
	"""
	return f"69{''.join([str(random.randint(0, 9)) for _ in range(8)])}"

def generate_phone(phone_code):
	"""
	Returns a 10-digit landline phone number.
	"""
	rest_digits = [str(random.randint(0, 9)) for _ in range(10-len(phone_code))]
	return f"{phone_code}{''.join(rest_digits)}"

def generate_fullname(gender):
	"""
	Returns a fullname (first and last name) based on
	given gender (male/female).
	"""
	lens = {
		'male': {
			'first': 5412,
			'last': 47829
		},
		'female': {
			'first': 7288,
			'last': 65270
		}
	}
	first_name_id = random.randint(1, lens[gender]['first'])
	last_name_id = random.randint(1, lens[gender]['last'])

	first_name = db[f"{gender}_first_names"].find_one(id=first_name_id)['first_name']
	last_name = db[f"{gender}_last_names"].find_one(id=last_name_id)['last_name']

	return first_name, last_name

def generate_age(gender):
	"""
	Returns random age and an age group based on
	given gender, according to images' distribution.
	"""
	age_groups = ['18_28', '29_38', '39_48', '49_58', '59_68']
	ages = {
		'18_28': (18, 28),
		'29_38': (29, 38),
		'39_48': (39, 48),
		'49_58': (49, 58),
		'59_68': (59, 68)
	}
	weights = {
		'female': [0.412, 0.335, 0.163, 0.072, 0.018],
		'male': [0.142, 0.357, 0.254, 0.175, 0.072]
	}

	age_group = random.choices(age_groups, weights[gender])[0]
	a, b = ages[age_group]
	age = random.randint(a, b)

	return age, age_group

def generate_image(gender, age_group):
	"""
	Returns an image url based on given gender and age group.
	"""
	table_name = f"{gender}_img"
	filenames = [item['file'] for item in db[table_name].find(age_group=age_group)]
	filename = random.choice(filenames)
	return filename

def generate_person():
	"""
	Generates a person's details and returns
	a dictionary with them.
	"""
	while True:
		try:
			gender = random.choice(['male', 'female'])
			fullname = generate_fullname(gender)
			first_name, last_name = fullname
			email = generate_email(fullname)
			cellphone = generate_cellphone()
			age, age_group = generate_age(gender)
			address, postal_code, region, phone_code = generate_place()
			phone = generate_phone(phone_code)
			img_src = generate_image(gender, age_group)
			break
		except:
			pass

	return {
		'gender': gender,
		'first': first_name,
		'last': last_name,
		'age': age,
		'email': email,
		'cell': cellphone,
		'phone': phone,
		'address': address,
		'region': region,
		'postal_code': postal_code,
		'img': img_src
	}