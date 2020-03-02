package dev.aubique.doitmvc.dao;

import dev.aubique.doitmvc.model.User;

import java.util.List;

public interface UserDAO {

    List<User> getAll();

    User getOne(String email);

    void add(User user);
}
