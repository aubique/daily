DROP TABLE IF EXISTS tense;
DROP TABLE IF EXISTS verb;

CREATE TABLE verb
(
    created_at            TIMESTAMP DEFAULT now(),
    infinitive            VARCHAR PRIMARY KEY,

    present_tense         VARCHAR,
    present_perfect_tense VARCHAR,
    imperfect_tense       VARCHAR,
    future_tense          VARCHAR
);

CREATE TABLE tense
(
    verb_name              VARCHAR REFERENCES verb (infinitive),
    tense_name             VARCHAR UNIQUE NOT NULL,
    first_person_singular  VARCHAR,
    second_person_singular VARCHAR,
    third_person_singular  VARCHAR,
    first_person_plural    VARCHAR,
    second_person_plural   VARCHAR,
    third_person_plural    VARCHAR
);


INSERT INTO verb (infinitive, present_tense, present_perfect_tense, imperfect_tense, future_tense)
VALUES ('faire', 'faire_pr', 'faire_pp', 'faire_im', 'faire_fu');
INSERT INTO verb (infinitive, present_tense, present_perfect_tense, imperfect_tense, future_tense)
VALUES ('aller', 'aller_pr', 'aller_pp', 'aller_im', 'aller_fu');
INSERT INTO verb (infinitive, present_tense, present_perfect_tense, imperfect_tense, future_tense)
VALUES ('pouvoir', 'pouvoir_pr', 'pouvoir_pp', 'pouvoir_im', 'pouvoir_fu');

INSERT INTO tense (verb_name, tense_name,
                   first_person_singular, second_person_singular, third_person_singular,
                   first_person_plural, second_person_plural, third_person_plural)
VALUES ('faire', 'faire_pr', 'je fais', 'tu fais', 'il fait', 'nous faisons', 'vous faites', 'ils font');
INSERT INTO tense(verb_name, tense_name, first_person_singular, second_person_singular, third_person_singular,
                  first_person_plural, second_person_plural, third_person_plural)
VALUES ('faire', 'faire_pp', E'j\'ai fait', 'tu as fait', 'il a fait', 'nous avons fait', 'vous avez fait',
        'ils ont fait');
INSERT INTO tense(verb_name, tense_name, first_person_singular, second_person_singular, third_person_singular,
                  first_person_plural, second_person_plural, third_person_plural)
VALUES ('faire', 'faire_im', 'je faisais', 'tu faisais', 'il faisait', 'nous faisons', 'vous faisiez',
        'ils faisaient');
INSERT INTO tense(verb_name, tense_name, first_person_singular, second_person_singular, third_person_singular,
                  first_person_plural, second_person_plural, third_person_plural)
VALUES ('faire', 'faire_fu', 'je ferai', 'tu feras', 'il fera', 'nous ferons', 'vous ferez',
        'ils feront');

INSERT INTO tense (verb_name, tense_name,
                   first_person_singular, second_person_singular, third_person_singular,
                   first_person_plural, second_person_plural, third_person_plural)
VALUES ('aller', 'aller_pr', 'je vais', 'tu vas', 'il va', 'nous allons', 'vous allez', 'ils vont');
INSERT INTO tense(verb_name, tense_name, first_person_singular, second_person_singular, third_person_singular,
                  first_person_plural, second_person_plural, third_person_plural)
VALUES ('aller', 'aller_pp', 'je suis allé', 'tu es allé', 'il est allé', 'nous sommes allés', 'vous êtes allés',
        'ils sont allés');
INSERT INTO tense(verb_name, tense_name, first_person_singular, second_person_singular, third_person_singular,
                  first_person_plural, second_person_plural, third_person_plural)
VALUES ('aller', 'aller_im', E'j\'allais', 'tu allais', 'il allait', 'nous allions', 'vous alliez',
        'ils allaient');
INSERT INTO tense(verb_name, tense_name, first_person_singular, second_person_singular, third_person_singular,
                  first_person_plural, second_person_plural, third_person_plural)
VALUES ('aller', 'aller_fu', E'j\'irai', 'tu iras', 'il ira', 'nous irons', 'vous irez',
        'ils iront');

INSERT INTO tense (verb_name, tense_name,
                   first_person_singular, second_person_singular, third_person_singular,
                   first_person_plural, second_person_plural, third_person_plural)
VALUES ('pouvoir', 'pouvoir_pr', 'je peux', 'tu peux', 'il peut', 'nous pouvons', 'vous pouvez', 'ils peuvent');
INSERT INTO tense(verb_name, tense_name, first_person_singular, second_person_singular, third_person_singular,
                  first_person_plural, second_person_plural, third_person_plural)
VALUES ('pouvoir', 'pouvoir_pp', E'j\'ai pu', 'tu as pu', 'il a pu', 'nous avons pu', 'vous avez pu',
        'ils ont pu');
INSERT INTO tense(verb_name, tense_name, first_person_singular, second_person_singular, third_person_singular,
                  first_person_plural, second_person_plural, third_person_plural)
VALUES ('pouvoir', 'pouvoir_im', 'je pouvais', 'tu pouvais', 'il pouvait', 'nous pouvions', 'vous pouviez',
        'ils pouvaient');
INSERT INTO tense(verb_name, tense_name, first_person_singular, second_person_singular, third_person_singular,
                  first_person_plural, second_person_plural, third_person_plural)
VALUES ('pouvoir', 'pouvoir_fu', 'je pourrai', 'tu pourras', 'il pourrai', 'nous pourrons', 'vous pourrez',
        'ils pourront');

SELECT infinitive
FROM verb;

-- SELECT tense.*
-- FROM verb
--          RIGHT JOIN tense ON verb.infinitive = tense.verb_name;

SELECT tense.*
FROM verb
         RIGHT JOIN tense ON verb.infinitive = tense.verb_name
WHERE verb.infinitive = 'pouvoir';
