import time

import redis


# pool = redis.ConnectionPool(host='10.33.3.217', port=6379, password='Dzhinternet!', db=0 , decode_responses=True)
pool = redis.ConnectionPool(host='10.15.108.95', port=6385, password='test', db=0 , decode_responses=True)

r = redis.Redis(connection_pool=pool)
def  changeteamphoto():
    result_length = 0
    for key in r.scan_iter(match='im_team_analyst_stock_team*', count=100):
        result_length += 1
        teamname = key.split(':')[1]
        # teamno = (r.zrange(key, 0, -1)[0]).split(':')[0]
        teamno = (list(r.smembers(key))[0]).split(':')[0]
        print(teamname)
        print("1111")
        print(teamno)
        # print("{}:{}".format(teamname ,teamno) )

def main():
    changeteamphoto()


if __name__ == '__main__':
    main()


