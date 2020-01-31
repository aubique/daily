import java.sql.*;
import java.util.Calendar;

public class jse_191210_2155 {

    private static final String INSERT_NEW = "INSERT INTO users (username,password,created) VALUES(?,?,?)";
    private static final String GET_ALL = "SELECT * FROM users;";
    private static final String DELETE_USER = String.format(
            "DELETE FROM users WHERE %s=?", Options.USERNAME_FIELD);

    public static void main(String[] args) {
        Connection conn = null;
        PreparedStatement insertStatement, getStatement, deleteStatement = null;

        try {
            Calendar calendar = Calendar.getInstance();
            conn = DriverManager.getConnection(Options.HOST, Options.USERNAME, Options.PASSWORD);

            deleteStatement = conn.prepareStatement(DELETE_USER);
            deleteStatement.setString(1, "Louis");

            insertStatement = conn.prepareStatement(INSERT_NEW);
            insertStatement.setString(1, "Louis");
            insertStatement.setString(2, "pa$$w0rd");
            insertStatement.setTimestamp(3, new Timestamp(calendar.getTime().getTime()));
            getStatement = conn.prepareStatement(GET_ALL);

            deleteStatement.execute();
            insertStatement.execute();
            ResultSet res = getStatement.executeQuery();

            while (res.next()) {
                int id = res.getInt(Options.ID_FIELD);
                String user = res.getString(Options.USERNAME_FIELD);
                String pass = res.getString(Options.PASSWORD_FIELD);
                Timestamp date = res.getTimestamp(Options.DATE_FIELD);
                User userObj = new User(id, user, pass, date);

                System.out.println(userObj.toString());
            }

        } catch (SQLException e) {
            System.out.println("We didn't get managed to establish MySQL connection");
        }
    }

    private static final class Options {
        public static final String ID_FIELD = "id";
        public static final String USERNAME_FIELD = "username";
        public static final String PASSWORD_FIELD = "password";
        public static final String DATE_FIELD = "created";
        public static final String HOST = "jdbc:mariadb://localhost:3306/devcolibri";
        public static final String USERNAME = "idea";
        public static final String PASSWORD = "idea";
    }
}

class User {

    private int id;
    private String username;
    private String password;
    private Timestamp date;

    User(int id, String username, String password, Timestamp date) {
        this.id = id;
        this.username = username;
        this.password = password;
        this.date = date;
    }

    User() {
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public Timestamp getDate() {
        return date;
    }

    public void setDate(Timestamp date) {
        this.date = date;
    }

    @Override
    public String toString() {
        return getClass().getSimpleName()
                + "{id:" + id
                + ",username:" + username
                + ",date:" + date.toString()
                + "}";
    }
}
