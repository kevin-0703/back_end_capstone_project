CINELIBRARY is a movie review api that was created using django and django REST framework. this api allows users to register, get authentication token, list movies from the api, get movies by id, create new movie and create reviews. This also possible by the help of OMDB API. Here is a guide of how to use the api using curl:

1. REGISTER USER:
   curl -X POST http://nshutikevin.pythonanywhere.com/cinemate/register/ \
   -H "Content-Type: application/json" \
   -d '{
   "username": "testuserkevin",
   "email": "testuser@example.com",
   "password": "securepassword123"
   }'

2. OBTAIN AUTHENTICATION TOKEN:
   curl -X POST http://nshutikevin.pythonanywhere.com/cinemate/auth/token/ \
   -H "Content-Type: application/json" \
   -d '{
   "username": "testuserkevin",
   "password": "securepassword123"
   }'

3. LIST ALL MOVIES:
   curl -H "Authorization: Token ..." \
   http://nshutikevin.pythonanywhere.com/cinemate/movies/

4.GET MOVIE BY ID:
curl -H "Authorization: Token ..." \
http://nshutikevin.pythonanywhere.com/cinemate/movies/1/

5. CREATE NEW MOVIE:
   curl -X POST http://nshutikevin.pythonanywhere.com/cinemate/movies/ \
   -H "Authorization: Token ..." \
   -H "Content-Type: application/json" \
   -d '{
   "title": "Mission Impossible",
   "description": "Action movie with spy missions",
   "release_date": "2023-07-15T00:00:00Z",
   "created_at": "2025-08-29T12:00:00Z"
   }'

6. LIST ALL REVIEWS:
   curl -H "Authorization: Token ..." \
   http://nshutikevin.pythonanywhere.com/cinemate/reviews/

7. CREATE REVIEW:
   curl -X POST http://nshutikevin.pythonanywhere.com/cinemate/reviews/ \
   -H "Authorization: Token ..." \
   -H "Content-Type: application/json" \
   -d '{
   "movie": 1,
   "rating": 5,
   "comment": "Amazing movie!"
   }'
