# roommate-rumble-backend

This is the backend for the TAMS Roommate Rumble web application.

## Algorithm

1. preload all user information (or preload computations if already done)
2. create user objects
3. loop through all users and calculate distance between each

distance = sqrt(wx^2 * wx^2 * ... * wx^2 * wx^2) where each wx is a distinct input dimension as well as its respective weight.

4. save computations
5. set up API endpoints via flask

## API Documentation

### /login
The login endpoint. (This is not fully figured out yet). TODO

### /fetch

The fetch endpoint. This will be a POST endpoint that will take some identifying information about the user. This information will either be the email or ID.
Fetch will return a JSON document with the ten closest users to the given ID.

### /taken

This endpoint will take in a boolean to either mark the user as "taken" or "not taken."


