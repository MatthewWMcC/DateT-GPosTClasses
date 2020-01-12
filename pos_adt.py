## @file pos_adt.py
#  @author First and Last Name
#  @brief ?
#  @date ?
from __future__ import absolute_import
import math
from date_adt import DateT


class GPosT:


    def __init__(self, long, lati):
        self.long = long
        self.lati = lati

    def lat(self):
        return self.lati
    def lon(self):
        return self.long
    
    def west_of(self, p):
        if self.long < p.long:
            return True
        else:
            return False
    def north_of(self, p):
        if self.lati > p.lati:
            return True
        else:
            return False
    def equal(self, p):
        R = 6371
        a = (math.sin(abs(p.lati - self.lati)/2)) ** 2 + math.cos(p.lati) * math.cos(self.lati) * (math.sin(abs(p.long - self.long)/2))
        d = R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        if d < 1:
            return True
        else:
            return False
    
    def move(self, b, d):
        R = 6371
        ang = d / R
        lati1 = math.radians(self.lati)
        long1 = math.radians(self.long)
        bearing = math.radians(b)
        lati2 = math.asin( math.sin(lati1) * math.cos(ang) + math.cos(lati1) * math.sin(ang) * math.cos(bearing) )
        self.long = self.long + math.atan2(math.sin(bearing) * math.sin(ang) * math.cos(lati1), math.cos(ang) - math.sin(lati1) * math.sin(lati2))
        self.lati = lati2
        self.long = math.degrees(self.long)
        self.lati = math.degrees(self.lati)
    def distance(self, p):
        R = 6371
        lati1 = math.radians(self.lati)
        long1 = math.radians(self.long)
        latip = math.radians(p.lati)
        longp = math.radians(p.long)
        a = (math.sin(abs(latip - lati1)/2)) ** 2 + math.cos(latip) * math.cos(lati1) * (math.sin(abs(longp - long1)/2))
        d = R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return d
    def arrival_date(self, p, d, s):
        dis = self.distance(p)
        
        days = int(dis / s)
        return d.add_days(days)

pos = GPosT(20, 60)
dest = GPosT(30, 60)
date = DateT(1, 1,2000)
speed = 0.5
endDate = pos.arrival_date(dest, date, speed)

print(endDate.d, endDate.m, endDate.y)
