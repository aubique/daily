package dev.aubique;

/**
 * Java 8 Groussard: Mise en œuvre avec Java
 * Polymorphism and static variables
 */
public class jse_191126_1342 {
    public static void main(String[] args) {
        Person[] chars = {
                new Employee("Boris", "Lisitsin"),
                new Employee("Dima", "Kirov")
        };
        for (Person emp : chars) {
            System.out.printf("Employee %-18sID: %d%n", emp.getFullName(), emp.getId());
        }
        System.out.printf("There are %d employees overall", Person.getPersons());
    }
}

abstract class Person {
    static private Integer persons = 1;
    private Integer id;

    Person() {
        this.id = persons++;
    }

    public static Integer getPersons() {
        return persons - 1;
    }

    public Integer getId() {
        return id;
    }

    public abstract String getName();

    public abstract void setName(String name);

    public abstract String getFullName();
}

class Employee extends Person {
    private String name;
    private String surname;

    Employee() {
        super();
        name = "";
        surname = "";
    }

    Employee(String name, String surname) {
        super();
        this.name = name;
        this.surname = surname;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public void setName(String name) {
        this.name = name;
    }

    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }

    @Override
    public String getFullName() {
        return getName() + " " + getSurname();
    }
}
