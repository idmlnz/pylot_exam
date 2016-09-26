use friendship;

SELECT u1.firstname, u1.lastname, u2.firstname AS friend_firstname, u2.lastname AS friend_lastname
  FROM users AS u1, users AS u2, friendship AS f
  WHERE u1.id = f.user_id
  AND u2.id = f.friend_id;
