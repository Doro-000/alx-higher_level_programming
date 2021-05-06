def roman_to_int(roman_string):
	if (not isinstance(roman_string, str)) or (not roman_string):
		return 0
	mappings = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
	result = 0
	for unit in roman_string:
		result += mappings[unit]
	for x in ["CD", "CM", "XL", "XC", "IV", "IX"]:
		if x in roman_string:
			result -= (2 * mappings[x[0]])
	return result
