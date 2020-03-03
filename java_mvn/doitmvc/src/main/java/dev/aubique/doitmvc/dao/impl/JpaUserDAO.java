package dev.aubique.doitmvc.dao.impl;

import dev.aubique.doitmvc.dao.UserDAO;
import dev.aubique.doitmvc.model.User;
import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Transactional;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.persistence.TypedQuery;
import java.util.List;

@Component
@Transactional(readOnly = true)
public class JpaUserDAO implements UserDAO {

    @PersistenceContext(unitName = "entityManagerFactory")
    private EntityManager entityManager;

    @Override
    public List<User> getAll() {
        return entityManager.createQuery(
                "SELECT u FROM User u", User.class
        ).getResultList();
    }

    @Override
    public User getOne(String email) {
        TypedQuery<User> q = entityManager.createQuery(
                "SELECT u FROM User u WHERE u.email = :email", User.class);
        q.setParameter("email", email);
        return q.getResultList()
                .stream()
                .findAny()
                .orElse(null);
    }

    @Override
    @Transactional
    public void add(User user) {
        entityManager.persist(user);
    }
}
