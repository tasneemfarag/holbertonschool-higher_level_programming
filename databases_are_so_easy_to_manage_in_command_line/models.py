import peewee

my_models_db = peewee.SqliteDatabase("my_models.db", pragmas=(('foreign_keys', True), ))

class BaseModel(peewee.Model):
	class Meta:
		database = my_models_db
		order_by = ('id', )

class School(BaseModel):
	name = peewee.CharField(128, null=False)

	def __str__(self):
		return "School: %s (%d)" % (self.name, self.id)

class Batch(BaseModel):
	school = peewee.ForeignKeyField(School, related_name="batches", on_delete="CASCADE")
	name = peewee.CharField(128, null=False)

	def __str__(self):
		return "Batch: %s (%d)" % (self.name, self.id)

class User(BaseModel):
	first_name = peewee.CharField(128, default="")
	last_name = peewee.CharField(128, null=False)
	age = peewee.IntegerField(null=False)

	def __str__(self):
		return "User: %s %s (%d)" % (self.first_name, self.last_name, self.id)

class Student(User):
	batch = peewee.ForeignKeyField(Batch, related_name="students", on_delete="CASCADE")

	def __str__(self):
		if len(self.last_name) == 0:
			return "Student: %s (%d) part of the batch: %s" % (self.first_name, self.id, self.batch)
		else:	
			return "Student: %s %s (%d) part of the batch: %s" % (self.first_name, self.last_name, self.id, self.batch)

class Exercise(BaseModel):
	SUBJECTS = {'math': "Math", 'english': "English", 'history': "History", 'c_prog': "C prog", 'swift_prog': "Swift prog" }
	student = peewee.ForeignKeyField(Student, related_name="exercises", on_delete="CASCADE")
	subject = peewee.CharField(128, choices=SUBJECTS)
	note = peewee.IntegerField(default=0)

	def __str__(self):
		return "Exercise: %s has %d in %s (%d)" % (self.student, self.note, self.subject, self.id)

