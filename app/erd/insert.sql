use friendship;

select * from users;
select * from friendship;


INSERT  INTO users(firstname, lastname, email, password, birthday,created_at, updated_at) values('Chris', 'Baker','chris@yahoo.com','chris','2016-09-25 15:26:28', '2016-09-25 15:26:28','2016-09-25 15:26:28');
INSERT  INTO users(firstname, lastname, email, password, birthday,created_at, updated_at) values('Diana', 'Smith','diana@yahoo.com','diana','2016-09-25 15:26:28', '2016-09-25 15:26:28','2016-09-25 15:26:28');
INSERT  INTO users(firstname, lastname, email, password, birthday,created_at, updated_at) values('James', 'Johnson','james@yahoo.com','james','2016-09-25 15:26:28', '2016-09-25 15:26:28','2016-09-25 15:26:28');
INSERT  INTO users(firstname, lastname, email, password, birthday,created_at, updated_at) values('Jessica', 'Davidson','jessica@yahoo.com','jessica','2016-09-25 15:26:28', '2016-09-25 15:26:28','2016-09-25 15:26:28');


INSERT  INTO friendship(id, user_id, friend_id, users_id) values(1, 1, 4,1);
INSERT  INTO friendship(id, user_id, friend_id, users_id) values(2, 1, 3,1);
INSERT  INTO friendship(id, user_id, friend_id, users_id) values(3, 1, 2,1);

INSERT  INTO friendship(id, user_id, friend_id, users_id) values(4, 2, 1,2);
INSERT  INTO friendship(id, user_id, friend_id, users_id) values(5, 3, 1,3);
INSERT  INTO friendship(id, user_id, friend_id, users_id) values(6, 4, 1,4);
