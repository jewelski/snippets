import sqlalchemy

# Create a connection string in the format:
# postgresql://user:password@host:port/database
conn = "postgresql://user:password@host:port/database"

# Create an engine using the connection string
engine = sqlalchemy.create_engine(conn)