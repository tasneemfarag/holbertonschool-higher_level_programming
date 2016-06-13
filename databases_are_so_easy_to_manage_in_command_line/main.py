from __future__ import division
import sys
from models import BaseModel, School, Batch, User, Student, Exercise

actions = ['create', 'print', 'insert', 'delete', 'print_batch_by_school', 'print_student_by_batch', 'print_student_by_school', 'print_family', 'age_average', 'change_batch', 'print_all', 'note_average_by_student', 'note_average_by_batch', 'note_average_by_school', 'top_batch', 'top_school']
if len(sys.argv) < 2:
	print 'Please enter an action'
elif sys.argv[1] not in actions:
	print 'Undefined action' + ' ' + sys.argv[1]
else:
	if sys.argv[1] == 'create':
		
		try:
			School.create_table()
		except peewee.OperationError:
			pass

		try:
			Batch.create_table()
		except peewee.OperationError:
			pass

		try:
			User.create_table()
		except peewee.OperationError:
			pass

		try:
			Student.create_table()
		except peewee.OperationError:
			pass
		try:
			Exercise.create_table()
		except peewee.OperationError:
			pass				
	elif sys.argv[1] == 'print':
		if len(sys.argv) >= 3:
			if sys.argv[2] == 'school':
				for school in School.select():	
					print school
			elif sys.argv[2] == 'batch':
				for batch in Batch.select():
					print batch
			elif sys.argv[2] == 'user':
				for user in User.select():
					print user
			elif sys.argv[2] == 'student':
				for student in Student.select():
					print student
			elif sys.argv[2] == 'exercise':
				for exercise in Exercise.select():
					print exercise					
	elif sys.argv[1] == 'insert':
		if sys.argv[2] == 'school':
			school = School.insert(name=sys.argv[3]).execute()
			print "New school: " + str(School.select().where(School.id==school).get())
		elif sys.argv[2] == 'batch':
			batch = Batch.insert(school=sys.argv[3], name=sys.argv[4]).execute()
			print "New batch: "	+ str(Batch.select().where(Batch.id==batch).get())
		elif sys.argv[2] == 'student':
			if len(sys.argv) == 6:
				student = Student.insert(batch=sys.argv[3], age=sys.argv[4], last_name='', first_name=sys.argv[5]).execute()
			else:		
				student = Student.insert(batch=sys.argv[3], age=sys.argv[4], last_name=sys.argv[5], first_name=sys.argv[6]).execute()
			print "New student: " + str(Student.select().where(Student.id==student).get())
		elif sys.argv[2] == 'exercise':
			exercise = Exercise.insert(student=sys.argv[3], subject=sys.argv[4],note=sys.argv[5]).execute()
			print "New exercise: " + str(Exercise.select().where(Exercise.id==exercise).get())
	elif sys.argv[1] == 'delete':
		if sys.argv[2] == 'school':
			if School.select().where(School.id==sys.argv[3]).count() == 0:
				print "Nothing to delete"
			else:
				print_school = "Delete: " + str(School.select().where(School.id==sys.argv[3]).get())	
				school = School.delete().where(School.id == sys.argv[3]).execute()
				print print_school
		elif sys.argv[2] == 'student':
			if Student.select().where(Student.id==sys.argv[3]).count() == 0:
				print "Nothing to delete"
			else:
				print_student = "Delete: " + str(Student.select().where(Student.id==sys.argv[3]).get())	
				student = Student.delete().where(Student.id == sys.argv[3]).execute()
				print print_student
		elif sys.argv[2] == 'batch':
			if Batch.select().where(Batch.id==sys.argv[3]).count() == 0:
				print "Nothing to delete"
			else:
				print_batch = "Delete: " + str(Batch.select().where(Batch.id==sys.argv[3]).get())	
				batch = Batch.delete().where(Batch.id == sys.argv[3]).execute()
				print print_batch
		elif sys.argv[2] == 'exercise':
			if Exercise.select().where(Exercise.id==sys.argv[3]).count() == 0:
				print "Nothing to delete"
			else:
				print_exercise = "Delete: " + str(Exercise.select().where(Exercise.id==sys.argv[3]).get())	
				exercise = Exercise.delete().where(Exercise.id == sys.argv[3]).execute()
				print print_exercise		
	elif sys.argv[1] == 'print_batch_by_school':
		if School.select().where(School.id==sys.argv[2]).count() == 0:
			print "School not found"
		else:
			school = School.select().where(School.id==sys.argv[2]).get()
			for batch in school.batches:
				print batch
	elif sys.argv[1] == 'print_student_by_batch':
		if Batch.select().where(Batch.id==sys.argv[2]).count() == 0:
			print "Batch not found"
		else: 
			batch = Batch.select().where(Batch.id==sys.argv[2]).get()
			for student in batch.students: 
				print student
	elif sys.argv[1] == 'print_student_by_school':
		if School.select().where(School.id==sys.argv[2]).count() == 0:
			print "School not found"
		else:
			school = School.select().where(School.id==sys.argv[2]).get()
			for batch in school.batches:
				for student in batch.students:
					print student
	elif sys.argv[1] == 'print_family':
		student_last = Student.select().where(Student.last_name==sys.argv[2])
		for student in student_last:
			print student
	elif sys.argv[1] == 'age_average':
		if len(sys.argv) > 2:
			batch = Batch.select().where(Batch.id==sys.argv[2]).get()
			count_students = 0
			sum_ages = 0
			for student in batch.students:
				count_students = count_students + 1
				sum_ages = sum_ages + student.age
			print str(sum_ages / count_students)	 
		else:
			count_students = 0
			sum_ages = 0
			for student in Student:
				count_students = count_students + 1
				sum_ages = sum_ages + student.age
			print str(sum_ages / count_students)	
	elif sys.argv[1] == 'change_batch':
		if Student.select().where(Student.id==sys.argv[2]).count() == 0:
			print "Student not found"
		if Batch.select().where(Batch.id==sys.argv[3]).count() == 0:
			print "Batch not found"
		student = Student.select().where(Student.id==sys.argv[2]).get()
		if student.batch.id == int(sys.argv[3]):
			print str(Student.select().where(Student.id==sys.argv[2]).get()) + " already in " + str(Batch.select().where(Batch.id==sys.argv[3]).get())
		else:
			Student.update(batch=Batch.select().where(Batch.id==sys.argv[3])).where(Student.id == sys.argv[2]).execute()
			print str(Student.select().where(Student.id==sys.argv[2]).get()) + " has been move to "	+ str(Batch.select().where(Batch.id==sys.argv[3]).get())
	elif sys.argv[1] == 'print_all':
		for school in School.select():
			print school
			for batch in school.batches:
				print "    " + str(batch)
				for student in batch.students:
					print "        " + str(student)					
					for exercise in student.exercises:
						print "            " + str(exercise)
	elif sys.argv[1] == 'note_average_by_student':
		if Student.select().where(Student.id==sys.argv[2]).count() == 0:
			print "Student not found"
		else:
			for exercise in Student.select().where(Student.id==sys.argv[2]).get().exercises:
				print exercise.subject + ": " + str(exercise.note)
	elif sys.argv[1] == 'note_average_by_batch':
		if Batch.select().where(Batch.id==sys.argv[2]).count() == 0:
			print "Batch not found"
		else:
			batch = Batch.select().where(Batch.id==sys.argv[2]).get()
			SUM_SUBJECTS = {'math': 0, 'english': 0, 'history': 0, 'c_prog': 0, 'swift_prog': 0 }
			NUM_SUBJECTS = {'math': 0, 'english': 0, 'history': 0, 'c_prog': 0, 'swift_prog': 0 }
			for student in batch.students:
				for exercise in student.exercises:
					for subject in Exercise.SUBJECTS:
						if Exercise.SUBJECTS[subject] == exercise.subject:
							SUM_SUBJECTS[subject] = SUM_SUBJECTS[subject] + exercise.note
							NUM_SUBJECTS[subject] = NUM_SUBJECTS[subject] + 1
			
			for subject in NUM_SUBJECTS:
				if NUM_SUBJECTS[subject] != 0:
					print Exercise.SUBJECTS[subject] + ": " + str(SUM_SUBJECTS[subject]/NUM_SUBJECTS[subject])
	elif sys.argv[1] == 'note_average_by_school':
		if School.select().where(School.id==sys.argv[2]).count() == 0:
			print "School not found"
		else:
			school = School.select().where(School.id==sys.argv[2]).get()
			SUM_SUBJECTS = {'math': 0, 'english': 0, 'history': 0, 'c_prog': 0, 'swift_prog': 0 }
			NUM_SUBJECTS = {'math': 0, 'english': 0, 'history': 0, 'c_prog': 0, 'swift_prog': 0 }
			for batch in school.batches:
				for student in batch.students:
					for exercise in student.exercises:
						for subject in Exercise.SUBJECTS:
							if Exercise.SUBJECTS[subject] == exercise.subject:
								SUM_SUBJECTS[subject] = SUM_SUBJECTS[subject] + exercise.note
								NUM_SUBJECTS[subject] = NUM_SUBJECTS[subject] + 1
			
			for subject in NUM_SUBJECTS:
				if NUM_SUBJECTS[subject] != 0:
					print Exercise.SUBJECTS[subject] + ": " + str(SUM_SUBJECTS[subject]/NUM_SUBJECTS[subject])
	elif sys.argv[1] == 'top_batch':
		if Batch.select().where(Batch.id==sys.argv[2]).count() == 0:
			print "Batch not found"
		if len(sys.argv) > 3:
			batch = Batch.select().where(Batch.id==sys.argv[2]).get()
			top_student_id_in_batch = 0
			top_notes = 0
			for student in batch.students:
				total_notes = 0
				for exercise in student.exercises:
					if exercise.subject == sys.argv[3]:
						total_notes = total_notes + exercise.note
				if total_notes > top_notes:
					top_notes = total_notes
					top_student_id_in_batch = student.id
			print Student.select().where(Student.id==top_student_id_in_batch).get()
		else:
			batch = Batch.select().where(Batch.id==sys.argv[2]).get()
			top_student_id_in_batch = 0
			top_notes = 0
			for student in batch.students:
				total_notes = 0
				for exercise in student.exercises:
					total_notes = total_notes + exercise.note
				if total_notes > top_notes:
					top_notes = total_notes
					top_student_id_in_batch = student.id
			print Student.select().where(Student.id==top_student_id_in_batch).get()
	elif sys.argv[1] == 'top_school':
		if School.select().where(School.id==sys.argv[2]).count() == 0:
			print "School not found"
		else:
			school = School.select().where(School.id==sys.argv[2]).get()
			top_student_id_in_batch = 0
			top_notes = 0
			for batch in school.batches:
				for student in batch.students:
					total_notes = 0
					for exercise in student.exercises:
						total_notes = total_notes + exercise.note
					if total_notes > top_notes:
						top_notes = total_notes
						top_student_id_in_batch = student.id
			print Student.select().where(Student.id==top_student_id_in_batch).get()
