package dev.aubique;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class Jar200127Mapper {

    public static void main(String[] args) {
        Mapper200127 toExecute = new Mapper200127();
        toExecute.collectObjects();
        toExecute.fillOutObjects();
        toExecute.showObject();
    }
}

class Mapper200127 {

    private static final String selectAllVerbs = "SELECT infinitive FROM verb";
    private static final String selectByInfinitive
            = "SELECT tense.* FROM verb RIGHT JOIN tense ON verb.infinitive=tense.verb_name WHERE verb.infinitive";
    private static final String url = "jdbc:postgresql://localhost:5432/conj";
    private static final String passwd = "idea";
    private List<String> verbNameList;
    private List<Entity200127> objectList;

    private static Entity200127 mapper(ResultSet rs, String infinitive) throws SQLException {
        List<List<String>> verbTenseList = new ArrayList<>();
        int j = 0;

        while (rs.next()) {
            List<String> tense = new ArrayList<>();
            System.out.println("\nIteration: " + j++);
            for (int i = 3; i < 9; i++) {
                System.out.println(rs.getString(i));
                tense.add(rs.getString(i));
            }
            verbTenseList.add(tense);
        }

        return new Entity200127(infinitive, verbTenseList.get(0), verbTenseList.get(1));
    }

    // onStartUp
    public void collectObjects() {
        String query = selectAllVerbs;
        String column = "infinitive";
        this.verbNameList = new ArrayList<>();

        try {
            Connection conn = DriverManager.getConnection(url, passwd, passwd);
            Statement stmt = conn.createStatement();
            // SELECT infinitive FROM verb
            ResultSet rsVerbNames = stmt.executeQuery(query);
            while (rsVerbNames.next()) {
                this.verbNameList.add(rsVerbNames.getString(column));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void fillOutObjects() {
        Entity200127 entity;
        this.objectList = new ArrayList<>();

        for (String infinitive : this.verbNameList) {
            // SELECT ... WHERE %s = '%s'
            String query = String.format("%s = \'%s\'", selectByInfinitive, infinitive);
            System.out.println(query);
            try {
                Connection conn = DriverManager.getConnection(url, passwd, passwd);
                Statement stmt = conn.createStatement();
                ResultSet rsObjectContent = stmt.executeQuery(query);

                entity = mapper(rsObjectContent, infinitive);
                this.objectList.add(entity);
                conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }

    public void showObject() {
        this.objectList.forEach(e -> System.out.println(e.toString()));
    }

    private static class Entity200127 {

        String inf;
        List<String> pr;
        List<String> pp;

        Entity200127(String inf, List<String> pr, List<String> pp) {
            this.inf = "faire";
            if (!inf.isEmpty()) {
                this.inf = inf;
            }
            this.pr = pr;
            this.pp = pp;
        }

        @Override
        public String toString() {
            return "Entity200127{" +
                    "inf='" + inf + '\'' +
                    ", pr=" + pr +
                    ", pp=" + pp +
                    '}';
        }
    }
}
