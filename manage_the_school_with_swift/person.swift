enum Subject {
	case Math
	case English
	case French
	case History
}

class Person {
	var first_name: String = ""
	var last_name: String = ""
	var age: Int = 0

	
	init (first_name: String, last_name: String, age: Int) {
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
	}

	func fullName() -> String {
		let full_name = first_name + " " + last_name
		return full_name
	} 
	
}

protocol Classify {
	func isStudent() -> Bool
} 

class Mentor: Person, Classify {
	func isStudent() -> Bool {
		return false
	}
	let subject: Subject 
	init(first_name: String, last_name: String, age: Int, subject: Subject = Subject.Math) {
		self.subject = subject
		super.init(first_name: first_name, last_name: last_name, age: age)
	}
	func stringSubject() -> String {
		switch subject {
		case Subject.Math:
			return "Math"
		case Subject.English:
			return "English"
		case Subject.French:
			return "French"
		case Subject.History:
			return "History"			
		}
	}
}
class Student: Person, Classify {
	func isStudent() -> Bool {
		return true
	}
}
class School {
	var name: String = ""
	var list_persons: [Person] = []

	init(name: String) {
		self.name = name
	}

	func addStudent(p: Person) -> Bool {
		if let s = p as? Student {
			if(s.isStudent() == true) {
				list_persons.append(p)
				return true	 
			} else {
				return false
			}
		}else{
			return false
		}
	}

	func addMentor(p: Person) -> Bool {
		if let m = p as? Mentor {
			if(	m.isStudent() == false) {
				list_persons.append(p)
				return true
			} else {
				return false
			}
		}else{
			return false
		}
	}

	func listStudents() -> [Person] {
		var list_students: [Person] = []
		for person in list_persons {
			if let _ = person as? Student {
				list_students.append(person)
			}
		}
		list_students = list_students.sort({ $0.age > $1.age })
		return list_students
	}

	func listMentors() -> [Person] {
		var list_mentors: [Person] = []
		for person in list_persons {
			if let _ = person as? Mentor {
				list_mentors.append(person)
			}
		}
		list_mentors = list_mentors.sort({ $0.age > $1.age })
		return list_mentors
	}

	func listMentorsBySubject(subject: Subject = Subject.Math) -> [Person] {
		var list_mentors_by_subject: [Person] = []
		for person in list_persons {
			if let m = person as? Mentor {
				if( m.subject == subject){
					list_mentors_by_subject.append(person)
				}
			} 
		}
		list_mentors_by_subject = list_mentors_by_subject.sort({ $0.age > $1.age })
		return list_mentors_by_subject
	}
}
