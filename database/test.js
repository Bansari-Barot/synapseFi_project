db.quote.insert({author:"shakespeare", quote:"To be or not to be..."})
db.createUser(
  {
    user: "admin",
    pwd: "password",
    roles: [ "readWrite", "dbAdmin" ]
  }
)
