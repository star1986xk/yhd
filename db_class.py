# -*- coding: utf-8 -*-
import pymysql
from settings import *


class db_class():

    def open(self):
        '''
        连接数据库
        @return:
        '''
        self.conn = pymysql.connect(**SQL)
        self.cursor = self.conn.cursor()
        self._sql = None

    def select_all(self, table_name):
        '''
        查询指定表全部数据
        @param table_name:表名
        @return:
        '''
        try:
            self._sql = 'SELECT * FROM %s;' % table_name
            self.cursor.execute(self._sql)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return None

    def select_count(self, table_name):
        '''
        查询指定表的数据条数
        @param table_name:表名
        @return:(条数,)
        '''
        try:
            self._sql = 'SELECT count(*) FROM %s;' % table_name
            self.cursor.execute(self._sql)
            result = self.cursor.fetchall()
            return result[0][0]
        except Exception as e:
            print(e)
            return None

    def select_count_condition(self, table_name, condition):
        '''
        条件查询\n
        如:select * from table1 where id=1 and name='xx';\n
        传参数：{'id':'1','name':'xx'}\n
        @param table_name: 表名
        @param condition:{'字段':'值',,,}
        @return: 查询后的数据集合
        '''
        try:
            self._sql = 'SELECT count(*) FROM ' + table_name + ' WHERE ' + \
                        ' AND '.join([k + '=%s' for k in condition.keys()]) + ';'
            self.cursor.execute(self._sql, tuple(condition.values()))
            result = self.cursor.fetchall()
            return result[0][0]
        except Exception as e:
            print(e)
            return None

    def select_condition(self, table_name, condition):
        '''
        条件查询\n
        如:select * from table1 where id=1 and name='xx';\n
        传参数：{'id':'1','name':'xx'}\n
        @param table_name: 表名
        @param condition:{'字段':'值',,,}
        @return: 查询后的数据集合
        '''
        try:
            self._sql = 'SELECT * FROM ' + table_name + ' WHERE ' + \
                        ' AND '.join([k + '=%s' for k in condition.keys()]) + ';'
            self.cursor.execute(self._sql, tuple(condition.values()))
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return None

    def select_uid(self, table_name):
        try:
            self._sql = "select distinct uid from " + table_name + ";"
            self.cursor.execute(self._sql)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return None

    def select_group_sum(self, table_name, uid_list, group_name, sum_name):
        '''
        分组查询求和
        :param table_name: 表名
        :param uid_list: 抓取id的列表
        :param group_name:分组字段
        :param sum_name:求和字段
        :return:查询结果
        '''
        try:
            self._sql = "select sum(" + sum_name + ")," + group_name + "  from " + table_name + " where uid in (" + ','.join(
                ['%s' for uid in uid_list]) + ") group by " + group_name + ";"
            self.cursor.execute(self._sql, uid_list)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return None

    def select_group_avg(self, table_name, uid_list, group_name, avg_name):
        '''
        分组查询平均值
        :param table_name: 表名
        :param uid_list: 抓取id的列表
        :param group_name:分组字段
        :param sum_name:均值字段
        :return:查询结果
        '''
        try:
            self._sql = "select avg(" + avg_name + ") as avg_m," + group_name + "  from " + table_name + " where uid in (" + ','.join(
                ['%s' for uid in uid_list]) + ") group by " + group_name + ";"
            self.cursor.execute(self._sql, uid_list)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return None

    def select_two_fields(self, table_name, uid_list, field1, field2):
        '''
        查询2个字段
        :param table_name: 表名
        :param uid_list: 抓取id的列表
        :param field1: 字段名
        :param field2: 字段名
        :return:查询结果
        '''
        try:
            self._sql = "select " + field1 + "," + field2 + " from " + table_name + " where uid in (" + ','.join(
                ['%s' for uid in uid_list]) + ");"
            self.cursor.execute(self._sql, uid_list)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return None

    def select_group_top10_sum(self, table_name, uid_list, group_name, sum_name):
        '''
        分组查询求和
        :param table_name: 表名
        :param uid_list: 抓取id的列表
        :param group_name:分组字段
        :param sum_name:求和字段
        :return:查询结果
        '''
        try:
            self._sql = "select sum(" + sum_name + ")," + group_name + "  from " + table_name + " where uid in (" + ','.join(
                ['%s' for uid in uid_list]) + ") group by " + group_name + " order by sum(sales) desc limit 0,10;"
            self.cursor.execute(self._sql, uid_list)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return None

    def select_group_top10_avg(self, table_name, uid_list, group_name, avg_name):
        '''
        分组查询求和
        :param table_name: 表名
        :param uid_list: 抓取id的列表
        :param group_name:分组字段
        :param sum_name:均值字段
        :return:查询结果
        '''
        try:
            self._sql = "select avg(" + avg_name + ")," + group_name + "  from " + table_name + " where uid in (" + ','.join(
                ['%s' for uid in uid_list]) + ") group by " + group_name + " order by sum(sales) desc limit 0,10;"
            self.cursor.execute(self._sql, uid_list)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return None

    def insert_many(self, table_name, obj_list):
        '''
        批量插入相同格式的一批数据\n
        如:\n
        insert table1(name,age) values('小明',30);\n
        insert table1(name,age) values('老王',30);\n
        可传参数:\n
        obj_list = [{'name':'小明','age':'10'},{'name':'老王','age':'30'}]\n
        @param table_name: 表名
        @param obj_list: [{'字段'：'值',,,},,,]
        @return: True|False
        '''
        try:
            self._sql = 'INSERT ' + table_name + '(' + ','.join([k for k in obj_list[0].keys()]) + ') VALUES(' + \
                        ','.join(['%s' for k in obj_list[0]]) + ');'
            datas = tuple(tuple(v for v in li.values()) for li in obj_list)
            self.cursor.executemany(self._sql, datas)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update_many(self, table_name, obj_list, condition_list):
        '''
        批量更新相同格式的一批数据\n
        如: \n
        update table1 set name='小明',age=10 where id=1;\n
        update table1 set name='老王',age=30 where id=2;\n
        可这样传参数:\n
        obj_list = [{'name':'小明','age':'10'},{'name':'老王','age':'30'}]\n
        condition_list = [{'id':'1'},{'id':'2'}]
        @param table_name: 表名
        @param obj_list: [{'字段'：'值',,,},,,]
        @param condition_list: [{'字段'：'值',,,},,,]
        @return:True|False
        '''
        try:
            self._sql = 'UPDATE ' + table_name + ' SET ' + ','.join(
                [k + '=%s' for k in obj_list[0].keys()]) + ' WHERE ' + \
                        ' and '.join([k + '=%s' for k in condition_list[0].keys()]) + ';'
            datas = tuple(
                tuple(obj.values()) + tuple(condition.values()) for obj, condition in zip(obj_list, condition_list))
            self.cursor.executemany(self._sql, datas)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete_many(self, table_name, condition_list):
        '''
        批量删除\n
        如：\n
        delete from table1 where id=1 and name='xxx'\n
        delete from table1 where id=3 and name='yy'\n
        可传参数\n
        condition_list = [{id:'1','name':'xxx'},{id:'3','name':'yy'}]
        @param table_name: 表名
        @param condition_list: [{'字段': '值',,,},,,]
        @return: True|False
        '''
        try:
            self._sql = 'DELETE FROM ' + table_name + ' WHERE ' + ' and '.join(
                [k + '=%s' for k in condition_list[0].keys()]) + ';'
            datas = tuple(tuple(condition.values()) for condition in condition_list)
            self.cursor.executemany(self._sql, datas)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def close(self):
        self.cursor.close()
        self.conn.close()
