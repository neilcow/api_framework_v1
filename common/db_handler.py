import pymysql
import yaml
from pymysql.cursors import DictCursor

from config.setting import DevConfig


class DBhandler():

    def __init__(self, host='127.0.0.1', port=3306,
                user='root', password='', charset='utf8',
                database='test', cursorclass=DictCursor, **kwargs):
        self.conn = pymysql.connect(host=host, port=port,
                                    database=database, user=user,
                                    password=password, charset=charset,
                                    cursorclass=cursorclass)
        self.cursor = self.conn.cursor()

    def query(self, sql, args, one=True):
        self.cursor.execute(sql, args)
        if one:
            return self.cursor.fetchone()
        else:
            return self.cursor.fetchall()

    def close(self):
        self.conn.close()
        self.cursor.close()


if __name__ == '__main__':
    config = DevConfig()
    f = open(config.yaml_config_path, encoding='utf-8')
    yaml_data = yaml.load(f, Loader=yaml.FullLoader)
    print(yaml_data)
    db = DBhandler(host=yaml_data['database']['host'],
                   port=yaml_data['database']['port'],
                   user=yaml_data['database']['user'],
                   password=yaml_data['database']['password'],
                   database=yaml_data['database']['database'],
                   charset=yaml_data['database']['charset'])
    res = db.query('select * from member', args=None)
    print(res)
