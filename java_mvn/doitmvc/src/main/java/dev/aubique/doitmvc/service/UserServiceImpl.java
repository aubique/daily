package dev.aubique.doitmvc.service;

import dev.aubique.doitmvc.model.User;
import dev.aubique.doitmvc.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
@Transactional(readOnly = true)
public class UserServiceImpl implements UserService {

    @Autowired
    private UserRepository userRepository;

    @Override
    public List<User> getAll() {
        return userRepository.findAll();
    }

    @Override
    public User getOne(String email) {
        return userRepository.findByEmail(email);
    }

    @Override
    @Transactional
    public void add(User user) {
        userRepository.save(user);
    }
}
