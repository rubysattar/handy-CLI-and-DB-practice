brew services stop postgresql@17      # stop the server
brew services restart postgresql@17   # restart it
psql postgres                         # open a shell on the default database
dropdb demo                           # delete a database