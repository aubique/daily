package dev.aubique.doitmvc.dao.impl;

import dev.aubique.doitmvc.dao.UserDAO;
import dev.aubique.doitmvc.model.User;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.io.InputStream;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

@Component
public class JdbcApiUserDAO implements UserDAO {

    private static Connection conn;

    static {
        String url = null;
        String username = null;
        String password = null;

        // load db properties
        try (InputStream in = UserDAO.class
                .getClassLoader().getResourceAsStream("persistence.properties")) {
            Properties properties = new Properties();
            properties.load(in);
            url = properties.getProperty("url");
            username = properties.getProperty("username");
            password = properties.getProperty("password");
        } catch (IOException e) {
            e.printStackTrace();
        }

        // acquire db connection
        try {
            Class.forName("org.postgresql.Driver");
            conn = DriverManager.getConnection(url, username, password);
        } catch (SQLException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    @Override
    public List<User> getAll() {
        List<User> users = new ArrayList<>();
        try {
            PreparedStatement ps = conn.prepareStatement("SELECT * FROM users");
            ResultSet rs = ps.executeQuery();
            while (rs.next()) {
                User user = new User();
                user.setName(rs.getString(1));
                user.setSurname(rs.getString(2));
                user.setEmail(rs.getString(3));
                users.add(user);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return users;
    }

    @Override
    public User getOne(String email) {
        try {
            PreparedStatement ps = conn.prepareStatement(
                    "SELECT * FROM users WHERE email = ?"
            );
            ps.setString(1, email);
            ResultSet rs = ps.executeQuery();
            if (rs.next()) {
                User user = new User();
                user.setName(rs.getString(1));
                user.setSurname(rs.getString(2));
                user.setEmail(rs.getString(3));
                return user;
            }
        } catch (SQLException ignored) {
        }
        return null;
    }

    @Override
    public void add(User user) {
        try {
            PreparedStatement ps = conn.prepareStatement("INSERT INTO users VALUES(?, ?, ?)");
            ps.setString(1, user.getName());
            ps.setString(2, user.getSurname());
            ps.setString(3, user.getEmail());
            ps.execute();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
