from influxdb import InfluxDBClient
client = InfluxDBClient(database='x')
#client.query('select * from "x"')
client.create_database("test2db")