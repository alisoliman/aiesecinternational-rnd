from sshtunnel import SSHTunnelForwarder
import psycopg2
from environs import Env
env = Env()
env.read_env()

def execute_sql(query_path, ep_id=None):
    if ep_id is None:
        str = read_path(query_path)
    else:
        str = read_path(query_path, ep_id)
    try:
        with SSHTunnelForwarder(
                ('internal.aiesec.org', 22),
                ssh_private_key=env('key_path'),
                ssh_username="ec2-user",
                remote_bind_address=(env('remote_bind_address'), 5432),
                local_bind_address=('localhost', 5430)) as server:

            server.start()
            print("Server connected")

            params = {
                'database': env('database'),
                'user': env('user'),
                'password': env('password'),
                'host': server.local_bind_host,
                'port': server.local_bind_port
            }

            conn = psycopg2.connect(**params)
            curs = conn.cursor()
            print("Database Connected")
            curs.execute(str)
            result = curs.fetchall()
            conn.close()
            return result

    except Exception as e:
        print("Connection Failed")
        print(e)


def read_path(query_path, ep_id=None):
    str = open(query_path, 'r').read()
    return (str % (ep_id))

        