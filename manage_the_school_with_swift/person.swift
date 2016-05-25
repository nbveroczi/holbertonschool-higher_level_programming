//Class
class Person {
    //public attributes
    var first_name: String
    var last_name: String
    var age: Int

    // Constructor
    init(first_name: String, last_name: String, age: Int) {
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    }
    // This func concats the first and last names
    func fullName() -> String {
        return first_name + " " + last_name
    }
    // This defines the className method for subclasses
    func className() -> String {
        return "Person"
    }
}
enum Subject {
    case Math
    case English
    case French
    case History
}
// This is the Classify protocol
protocol Classify {
    func isStudent() -> Bool
}
// This is the subclass of the Person Class with the Classify protocol
class Mentor: Person, Classify {
    // This is a method that returns class
    override func className () -> String {
        return "Mentor"
    }
    // This is the isStudent method
    func isStudent() -> Bool {
        return false
    }
    var subject: Subject

    // Constructor with subject
    init(first_name: String, last_name: String, age: Int, subject:
        Subject = Subject.Math) {
        self.subject = subject
        super.init(first_name: first_name, last_name: last_name, age:  age)
    }
    // This is a function which returns the subject
    func stringSubject() -> String {
        if self.subject == Subject.Math {
            return "Math"
        }
        if self.subject == Subject.English {
            return "English"
        }
        if self.subject == Subject.French {
            return "French"
        }
        if self.subject == Subject.History {
            return "History"
        }
        return "String"
    }
}
// This is another subclass of the Person Class
class Student: Person, Classify {
    override func className () -> String {
        return "Student"
    }
    func isStudent() -> Bool {
        return true
    }
}
