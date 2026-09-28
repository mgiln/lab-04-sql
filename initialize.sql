
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(200),
    time_of DATETIME
);
CREATE TABLE posts (
    post_id INT PRIMARY KEY,
    user_id INT,
    post_title VARCHAR(200),
    post_message TEXT,
    post_location TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users VALUES (1, 'Mgiln', 'maggie@gmail.com', '2026-08-29 09:08:00');
INSERT INTO users VALUES (2, 'r3bbca', 'r3bbca@gmail.com', '2026-09-20 10:12:00');
INSERT INTO users VALUES (3, 'han_s1', 'hanson111@yahoo.com', '2026-09-05 08:09:00');
INSERT INTO users VALUES (4, 'doggylovr', 'doggylovr@outlook.com', '2026-09-21 02:45:00');
INSERT INTO users VALUES (5, 'notjon22', 'jonP22@gmail.com', '2026-09-01 02:30:00');
INSERT INTO users VALUES (6, 'mchle57', 'michelle57@yahoo.com', '2026-08-30 06:55:00');
INSERT INTO users VALUES (7, 'cor3y09', 'correy09@outlook.com', '2026-09-24 09:07:00');
INSERT INTO users VALUES (8, 'sodaluvr', 'emily4lfye@gmail.com', '2026-09-12 12:30:00');
INSERT INTO users VALUES (9, 'elizabethjones', 'elizabethjones@gmail.com', '2026-09-10 01:00:00');
INSERT INTO users VALUES (10, 'jimmy77', 'jimmy77@yahoo.com', '2026-09-03 04:20:00');

INSERT INTO posts VALUES (1, 1, 'Best hike ever!', 'went on this strenous hike this weekend, but the view was worth it!', 'Shenandoah Park');
INSERT INTO posts VALUES (2, 2, 'Nails done', 'got a fresh set of nails done this past week!', 'Charlottesville');
INSERT INTO posts VALUES (3, 3, 'My dog', 'look at tucker lol', 'Richmond');
INSERT INTO posts VALUES (4, 4, 'Toy', 'Saw this really cute dog toy the other day, couldnt afford it though :( ', 'Springfield');
INSERT INTO posts VALUES (5, 5, 'Best game', 'whoever dislikes minecraft, come fight me', 'Richmond');
INSERT INTO posts VALUES (6, 6, 'Plushie', 'this plushie is soooo cute, im so glad i got it', 'Yorktown');
INSERT INTO posts VALUES (7, 7, 'Practice', 'coach said im gonna be benched next game.', 'Blacksburg');
INSERT INTO posts VALUES (8, 8, 'New Drink', 'Has anyone actually tried this new drink? Havent heard much about it tbh', 'Harrisonburg');
INSERT INTO posts VALUES (9, 9, 'New book', 'Just got this new book from the local bookstore, cant wait to read it! ', 'New York City');
INSERT INTO posts VALUES (10, 10, 'Work', 'I hate my job, cant wait to put in my two weeks.', 'Rockville');


