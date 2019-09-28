import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from yelp_scrapy.items import UserItem, BizItem

class YelpScrapyPipeline(object):

    def __init__(self):
        self.host = 'postgres'
        self.user = 'postgres'
        self.passwd = 'postgres'
        self.db = 'yelp_reviews'
        self.port = 5432

    def open_spider(self, spider):
        self.conn = psycopg2.connect(host=self.host,
                                     user=self.user,
                                     port=self.port,
                                     password=self.passwd)

        self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.cursor = self.conn.cursor()

        self.cursor.execute("DROP DATABASE IF EXISTS yelp_reviews;")
        self.cursor.execute("CREATE DATABASE yelp_reviews;")

        query = """
                CREATE TABLE IF NOT EXISTS biz (
                  id int GENERATED BY DEFAULT AS IDENTITY NOT NULL PRIMARY KEY,
                  name VARCHAR(255),
                  city VARCHAR(255),
                  zipcode VARCHAR(10),
                  state VARCHAR(3),
                  link VARCHAR(255),
                  star_raiting VARCHAR(4)
                  );

                CREATE TABLE IF NOT EXISTS
                reviewers (
                  id INT NOT NULL,
                  user_url VARCHAR(255),
                  star_raiting VARCHAR(4),
                  location VARCHAR(255),
                  state VARCHAR(3),
                  review_text TEXT,
                  review_date VARCHAR(10)
                  );
                """

        self.cursor.execute(query)
        self.conn.commit()

    def get_value(self, query):
        self.cursor.execute(query)
        record = self.cursor.fetchone()
        if len(record) == 1:
            record = record[0]
            return record
        else:
            raise ValueError('More than one value for record'
                             ' {record}'.format(record=record))

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

    def save_biz(self, item):
        query = """INSERT INTO biz (name, city, zipcode,
                                    state, link, star_raiting)
                VALUES (%s, %s, %s, %s, %s, %s)"""

        values = (item['business_name'], item['business_city'],
                  item['business_zip'], item['business_state'],
                  item['business_url'], item['business_star_rating'])

        self.cursor.execute(query, values)
        self.conn.commit()
        return item

    def save_user(self, item):
        biz_id = self.get_value("SELECT currval('biz_id_seq')")

        query = """INSERT INTO reviewers (id, user_url, star_raiting, location,
                                          review_text, review_date)
        VALUES (%s, %s, %s, %s, %s, %s)"""

        values = (biz_id, item['user_url'], item['review_raiting'],
                  item['reviewer_location'], item['review_text'],
                  item['review_date'])

        self.cursor.execute(query, values)

        self.conn.commit()
        return item

    def process_item(self, item, spider):

        if isinstance(item, BizItem):
            self.save_biz(item)

        if isinstance(item, UserItem):
            self.save_user(item)
