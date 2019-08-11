from influxdb import InfluxDBClient
db = InfluxDBClient(database='x')
db = InfluxDBClient('localhost', 8086, 'root', 'root', 'AccessHistory')
db.create_database("AccessHistory")
loginEvents = [{"measurement": "UserLogins",
               "tags": {
                   "Area": "North America",
                   "Location": "New York City",
                   "ClientIP": "192.168.0.256"
               },
               "fields":
                   {
                       "SessionDuration": 1.2
                   }
               },
              {"measurement": "UserLogins",
               "tags": {
                   "Area": "South America",
                   "Location": "Lima",
                   "ClientIP": "192.168.1.256"
               },
               "fields":
                   {
                       "SessionDuration": 2.0
                   }
              }]
db.write_points(loginEvents)