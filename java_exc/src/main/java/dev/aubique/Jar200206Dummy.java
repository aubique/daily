package dev.aubique;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.*;
import java.util.stream.Collectors;

public class Jar200206Dummy {

    public static final String URL = "jdbc:postgresql://localhost:5432/conj";
    public static final String PASSWD = "idea";
    public static final String DRIVER = "org.postgresql.Driver";

    public static void insertDummy() throws ClassNotFoundException, SQLException {
        Class.forName(DRIVER);
        Connection conn = DriverManager.getConnection(URL, PASSWD, PASSWD);
        Statement stmt = conn.createStatement();

        Spec200206 spec = new Spec200206(new DummyBuilder200206().construct());
        while (spec.hasNextQuery()) {
            stmt.execute(spec.toSqlQuery());
        }
    }

    public static void main(String[] args) {
        try {
            insertDummy();
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        }
    }
}

// SqlSpecification
class Spec200206 {

    private final List<String> TENSE_TABLE_COLUMNS = new ArrayList<>(Arrays.asList(Config200206.TENSE_COLS));
    private List<String> queries;
    private Iterator<String> iter;

    public Spec200206(Dummy200206 dummyObj) {
        this.queries = new ArrayList<>();
        this.constructQueries(dummyObj);
        this.iter = queries.iterator();
    }

    private void constructQueries(Dummy200206 dummyObj) {
        List<String> tenseFields = new ArrayList<>();
        tenseFields.add(dummyObj.presentField);
        tenseFields.add(dummyObj.presentPerfectField);
        tenseFields.add(dummyObj.imperfectField);
        tenseFields.add(dummyObj.futureField);

        String insertVerb = String.format("INSERT INTO verb"
                + "(infinitive,present_tense,present_perfect_tense,imperfect_tense,future_tense)"
                + "VALUES(\'%1$s\',\'%1$s_pr\',\'%1$s_pp\',\'%1$s_im\',\'%1$s_fu\')", dummyObj.verbName);
        this.queries.add(insertVerb);

        for (String field : tenseFields) {
            String insertTense = String.format(
                    "INSERT INTO tense (%s) VALUES (%s)",
                    String.join(",", TENSE_TABLE_COLUMNS),
                    dummyObj.getTenseListByTenseId(field).stream()
                            .map(value -> String.format("\'%s\'", value.replace("'", "''")))
                            .collect(Collectors.joining(","))
            );
            this.queries.add(insertTense);
        }

        try {
            System.out.println(new ObjectMapper().writerWithDefaultPrettyPrinter().writeValueAsString(queries));
        } catch (JsonProcessingException ignored) {
        }
    }

    public String toSqlQuery() {
        return iter.next();
    }

    public boolean hasNextQuery() {
        return this.iter.hasNext();
    }
}

// Entity
class Dummy200206 {

    private static final String presentSuffix = "_pr";
    private static final String presentPerfectSuffix = "_pp";
    private static final String imperfectSuffix = "_im";
    private static final String futureSuffix = "_fu";

    public String verbName;
    public String presentField;
    public String presentPerfectField;
    public String imperfectField;
    public String futureField;

    public List<String> presentTenseList;
    public List<String> presentPerfectTenseList;
    public List<String> imperfectTenseList;
    public List<String> futureTenseList;


    public Dummy200206(String verbName) {
        this.verbName = verbName;
        this.presentField = verbName + presentSuffix;
        this.presentPerfectField = verbName + presentPerfectSuffix;
        this.imperfectField = verbName + imperfectSuffix;
        this.futureField = verbName + futureSuffix;
    }

    public Dummy200206(
            String verbName,
            List<String> presentTenseList,
            List<String> presentPerfectTenseList,
            List<String> imperfectTenseList,
            List<String> futureTenseList
    ) {
        this(verbName);
        this.presentTenseList = presentTenseList;
        this.presentPerfectTenseList = presentPerfectTenseList;
        this.imperfectTenseList = imperfectTenseList;
        this.futureTenseList = futureTenseList;
    }

    public Map<String, Map<String, List<String>>> asDictionary() {
        Map<String, Map<String, List<String>>> dict = new TreeMap<>();
        Map<String, List<String>> tenses = new TreeMap<>();

        tenses.put(presentField, presentTenseList);
        tenses.put(presentPerfectField, presentPerfectTenseList);
        tenses.put(imperfectField, imperfectTenseList);
        tenses.put(futureField, futureTenseList);

        dict.put(verbName, tenses);
        return dict;
    }

    public List<String> getTenseListByTenseId(String tenseId) {
        List<String> tenseList = new ArrayList<>();
        String verbId = tenseId.substring(0, tenseId.length() - 3);

        tenseList.add(verbId);
        tenseList.add(tenseId);
        tenseList.addAll(this.asDictionary().get(verbId).get(tenseId));

        return tenseList;
    }
}

// Builder
class DummyBuilder200206 {

    private static String verbName = "manger";
    public Dummy200206 dummy;

    private static List<String> getPresentTenseList() {
        String[] presentTense = {
                "je mange",
                "tu mange",
                "il mange",
                "nous mangons",
                "vous mangez",
                "ils mangent"
        };
        return new ArrayList<>(Arrays.asList(presentTense));
    }

    private static List<String> getFutureTenseList() {
        String[] presentTense = {
                "je mangerai",
                "tu mangeras",
                "il mangera",
                "nous mangerons",
                "vous mangerez",
                "ils mangeront"
        };
        return new ArrayList<>(Arrays.asList(presentTense));
    }

    private static List<String> getImperfectTenseList() {
        String[] presentTense = {
                "je mangeais",
                "tu mangeais",
                "il mangeait",
                "nous mangions",
                "vous mangiez",
                "ils mangeaient"
        };
        return new ArrayList<>(Arrays.asList(presentTense));
    }

    private static List<String> getPresentPerfectTenseList() {
        String[] presentTense = {
                "j'ai mangé",
                "tu as mangé",
                "il as mangé",
                "nous avons mangé",
                "vous avez mangé",
                "ils ont mangé"
        };
        return new ArrayList<>(Arrays.asList(presentTense));
    }

    public Dummy200206 construct() {
        this.dummy = new Dummy200206(
                verbName,
                getPresentTenseList(),
                getPresentPerfectTenseList(),
                getImperfectTenseList(),
                getFutureTenseList()
        );

        return dummy;
    }
}

class Config200206 {

    public static final String[] TENSE_COLS = {
            "verb_name",
            "tense_name",
            "first_person_singular",
            "second_person_singular",
            "third_person_singular",
            "first_person_plural",
            "second_person_plural",
            "third_person_plural"
    };
    public static final String[] VERB_COLS = {
            "infinitive",
            "present_tense",
            "present_perfect_tense",
            "imperfect_tense",
            "future_tense"
    };
}
