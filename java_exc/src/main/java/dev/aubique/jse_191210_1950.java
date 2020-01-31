package dev.aubique;

import java.sql.*;

/**
 * Example: How to get SQL query
 */
public class jse_191210_1950 {
    private static final String HOST = "jdbc:mariadb://localhost:3306/mysql";
    private static final String USER = "root";
    private static final String PASS = "1234";
    private static final String QUERY = "SELECT * FROM users;";

    public static void main(String[] args) throws SQLException {
        Connection c = DriverManager.getConnection(HOST, USER, PASS);
        Statement s = c.createStatement();
        ResultSet rs = s.executeQuery(QUERY);
        while (rs.next()) {
            System.out.println(rs.getInt(1));
        }
    }
}
