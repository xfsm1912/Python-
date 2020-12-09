import MySQLdb


def test_pymysql():
    # not localhost, access denied
    # before run the code, run the mysql first by 'mysql -h 127.0.0.1 -u root -p'
    conn = MySQLdb.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='123456',
        db='mysql'
    )

    cur = conn.cursor()
    cur.execute('''
            CREATE TABLE price (                
                timestamp TIMESTAMP NOT NULL,                
                BTCUSD FLOAT(8,2),                
                PRIMARY KEY (timestamp)            
            );
        ''')
    cur.execute('''
        INSERT INTO price VALUES(
            "2019-07-14 14:12:17", 
            11234.56
        );
        ''')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    test_pymysql()
