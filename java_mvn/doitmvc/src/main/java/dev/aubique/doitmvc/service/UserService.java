package dev.aubique.doitmvc.service;

import dev.aubique.doitmvc.model.User;

import java.util.List;

public interface UserService {

    List<User> getAll();

    User getOne(String email);

    void add(User user);
}
