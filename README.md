# roommate-rumble-backend

This is the backend for the TAMS Roommate Rumble web application.

## Dev Setup

1. Make sure you have python3 installed
2. run the setup script
    - run setup.sh if on linux / OS X
    - run setup.bat on windows
3. You have a flask python3 environment set up!

Make sure you use the bins from the /env folder made by the setup script.

run `source env/bin/activate` on linux / OS X
or
run `env\Scripts\activate.bat` on windows to automatically use the env bins.

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


