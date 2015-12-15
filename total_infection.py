from nodes import Coach

"""
The total infection algorithm. Infects entire classroom in a 
depth-first traversal of the class. 
"""
def total_infection(coach):
	if isinstance(coach, Student) or coach.coach is not None:
		total_infection(coach.coach)
	coach.infect()
	s = [coach]
	while s:
		v = s.pop()
		v.infect()
		if isinstance(v, Coach):
			for student in v.students:
				s.append(student)