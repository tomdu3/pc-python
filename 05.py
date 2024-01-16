# Data Filter: Write a function that takes a list of dictionaries (representing people, with keys for name, age, and profession) and a profession string, and returns a new list with dictionaries where the profession matches the given string.

def filter_by_profession(people, profession):
	return [person for person in people if person['profession'] == profession]

people_data = [
  {
    "name": "Tom",
    "age": 45,
    "profession": "software developer"
  },
  {
    "name": "Charles",
    "age": 44,
    "profession": "hr administrator"
  },
  {
    "name": "Emily",
    "age": 30,
    "profession": "marketing manager"
  },
  {
    "name": "Sarah",
    "age": 35,
    "profession": "teacher"
  },
  {
    "name": "John",
    "age": 28,
    "profession": "graphic designer"
  },
  {
    "name": "Michael",
    "age": 40,
    "profession": "software developer"
  },
  {
    "name": "Elizabeth",
    "age": 38,
    "profession": "hr administrator"
  },
  {
    "name": "David",
    "age": 32,
    "profession": "marketing manager"
  },
  {
    "name": "Jessica",
    "age": 29,
    "profession": "teacher"
  },
  {
    "name": "Jennifer",
    "age": 33,
    "profession": "graphic designer"
  },
  {
    "name": "Robert",
    "age": 42,
    "profession": "software developer"
  },
  {
    "name": "Sophia",
    "age": 31,
    "profession": "hr administrator"
  },
  {
    "name": "William",
    "age": 36,
    "profession": "marketing manager"
  },
  {
    "name": "Olivia",
    "age": 27,
    "profession": "teacher"
  },
  {
    "name": "Daniel",
    "age": 39,
    "profession": "graphic designer"
  },
  {
    "name": "Emma",
    "age": 34,
    "profession": "software developer"
  },
  {
    "name": "Liam",
    "age": 29,
    "profession": "hr administrator"
  },
  {
    "name": "Ava",
    "age": 37,
    "profession": "marketing manager"
  },
  {
    "name": "Matthew",
    "age": 41,
    "profession": "teacher"
  },
  {
    "name": "Oliver",
    "age": 30,
    "profession": "graphic designer"
  }
]

print(filter_by_profession(people_data, 'teacher'))