SELECT 
users.user_id,
users.username, 
posts.post_id,
posts.post_title,
posts.post_location,
posts.post_message
FROM users
JOIN posts ON users.user_id = posts.user_id
WHERE posts.post_location = "Springfield"
