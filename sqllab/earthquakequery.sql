[lumbud@stearns sqllab]$ add *
-bash: add: command not found
[lumbud@stearns sqllab]$ git add *
[lumbud@stearns sqllab]$ git commit -m "added earthquakequery.sql and finalised the comments in it"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: empty ident name (for <lumbud@stearns.mathcs.carleton.edu>) not allowed
[lumbud@stearns sqllab]$ vi earthquakequery.sql 





-- This below gives us earthquakes ordered by magnitude
SELECT * FROM earthquakes ORDER BY mag DESC;

-- This below gives us the value of the average magnitude of the earthquakes
SELECT AVG(mag) FROM earthquakes;

-- This below gives us earthquakes with a depth greater than 30 and a magnitude greater than 4.5:

SELECT * FROM earthquakes WHERE quakedepth > 25 AND mag > 4.5;


~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
-- INSERT --

