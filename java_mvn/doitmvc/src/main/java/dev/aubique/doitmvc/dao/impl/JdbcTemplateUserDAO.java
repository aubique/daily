package dev.aubique.doitmvc.dao.impl;

import dev.aubique.doitmvc.dao.UserDAO;
import dev.aubique.doitmvc.model.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class JdbcTemplateUserDAO implements UserDAO {

    @Autowired
    private JdbcTemplate jdbcTemplate;

    public List<User> getAll() {
        return jdbcTemplate.query(
                "SELECT * FROM users",
                new BeanPropertyRowMapper<>(User.class)
        );
//        return jdbcTemplate.query("SELECT * FROM users", (resultSet, i) -> {
//            User user = new User();
//            user.setName(resultSet.getString(1));
//            user.setSurname(resultSet.getString(2));
//            user.setEmail(resultSet.getString(3));
//            return user;
//        });
    }

    public User getOne(String email) {
        return jdbcTemplate.query(
                "SELECT * FROM users WHERE email = ?",
                new Object[]{email},
                new BeanPropertyRowMapper<>(User.class)
        )
                .stream()
                .findAny()
                .orElse(null);
    }

    public void add(User user) {
        jdbcTemplate.update(
                "INSERT INTO users VALUES(?,?,?)",
                user.getName(), user.getSurname(), user.getEmail()
        );
    }
}
