package dev.aubique.doitmvc.dao.impl;

import dev.aubique.doitmvc.dao.UserDAO;
import dev.aubique.doitmvc.model.User;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.query.Query;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class HibernateUserDAO implements UserDAO {

    @Autowired
    private SessionFactory sessionFactory;

    private Session currentSession() {
        return sessionFactory.openSession();
    }

    @Override
    public List<User> getAll() {
        return currentSession().createQuery("FROM User", User.class).list();
    }

    @Override
    public User getOne(String email) {
        Query<User> q = currentSession().createQuery("FROM User WHERE email = :email", User.class);
        q.setParameter("email", email);
        return q.list()
                .stream()
                .findAny()
                .orElse(null);
    }

    @Override
    public void add(User user) {
        currentSession().save(user);
    }
}
