## @file date_adt.py
#  @author First and Last Name
#  @brief ?
#  @date ?

## @brief An ADT ...

def isLeap(ye):
    if (ye % 4 == 0 and ye % 100 != 0)  or ye % 400 == 0:
          return True
    else:
          return False 
class DateT:

  ## @brief ?
  #  @details ?
  #  @param m ...

  
  def __init__(self, d, m, y):
    self.y = y
    self.m = m
    self.d = d
    
  ## @brief ?
  #  @return ?
  def day(self):
    return self.d
  def month(self):
    return self.m
  def year(self):
    return self.y
  
  ##made next cleaner and more effective
  def next(self):
    dn = self.d
    mn = self.m
    yn = self.y
    du = dn
    mu = mn
    yu = yn
    if (mn == 2) and ((isLeap(yn) == True and dn == 29) or (isLeap(yn) == False and dn == 28)):
      du = 1
      mu = 3
      
    elif (mn == 1 or mn == 3 or mn == 5 or mn == 7 or mn == 8 or mn == 10) and dn == 31:
      du = 1
      mu = mn + 1
      
    elif (mn == 12) and dn == 31:
      du = 1
      mu = 1
      yu = yn + 1
    elif (mn == 4 or mn == 6 or mn == 9 or mn == 11) and dn == 30:
      mu = mn + 1
      du = 1
    else:
      
      du = dn + 1
      


    nextday = DateT(du, mu, yu)
    return nextday
  
  #Only finished next and part of prev
  def prev(self):
    dn = self.d
    mn = self.m
    yn = self.y
    du = dn
    mu = mn
    yu = yn
    if (dn == 1) and (mn == 2 or mn == 4 or mn == 6 or mn == 8 or mn == 9 or mn == 11):
      du = 31
      mu = mn - 1
    elif (dn == 1) and (mn == 5 or mn == 7 or mn == 10 or mn == 12):
      du = 30
      mu = mn - 1
    elif (dn == 1) and mn == 3 and isLeap(yn) == True:
      du = 29
      mu = 2
    elif (dn == 1) and mn == 3 and isLeap(yn) == False:
      du = 28
      mu = 2
    elif (dn == 1) and mn == 1:
      yu = yn - 1
      du = 31
      mu = 12
    else:
      du = dn - 1
    
    prevday = DateT(du, mu, yu)
    return prevday
  
  ##added before and after capabilities
  def before(self, d):
    if (self.y == d.y and self.m == d.m and self.d < d.d) or (self.y == d.y and self.m < d.m) or (self.y < d.y):
      return True
    else:
      return False
  def after(self, d):
    if (d.y == self.y and d.m == self.m and d.d < self.d) or (d.y == self.y and d.m < self.m) or (d.y < self.y):
      return True
    else:
      return False  
  def equal(self, d):
    if d.y == self.y and d.m == self.m and d.d == self.d:
      return True
    else:
      return False
  # etc.
  def days_between(self, d):
    x = 0
    if (self.equal(d) == True):
      
      return 0
    
    if (self.after(d) == True):
      
      while (self.equal(d) == False):
        
        self = self.prev()
        x += 1
      return x 
    if (self.before(d) == True):
      
      while (self.equal(d) == False):
        self = self.next()
        
        x += 1
      return x 

  def add_days(self, n):
    add = self
    for i in range(n):
      add = add.next()
    return DateT(add.d, add.m, add.y)
      
  

day = DateT(1,1,2000)
day2 = DateT(1,1,2001)

print(day.days_between(day2))