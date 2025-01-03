""" Lab 6: OOP and Inheritance"""
import random

# ANSWER QUESTION q1

# ANSWER QUESTION q2

#####################
# Required Problems #
#####################

class PrintModule:
    def pp(self):
        pretty_print(self)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.add_funds(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.stock = 0
        self.balance = 0

    def vend(self):
        if self.stock == 0:
            return "Machine is out of stock."
        if self.balance < self.price:
            required = self.price - self.balance
            return "You must add ${} more funds.".format(required)
        self.stock -= 1
        change = self.balance - self.price
        self.balance = 0
        if change > 0:
            return "Here is your {} and ${} change.".format(self.name, change)
        return "Here is your {}.".format(self.name)

    def add_funds(self, fund):
        if self.stock == 0:
            return "Machine is out of stock. Here is your ${}.".format(fund)
        self.balance += fund
        return "Current balance: ${}".format(self.balance)

    def restock(self, amount):
        self.stock += amount
        return "Current {} stock: {}".format(self.name, self.stock)





class Pet:
    """A pet.

    >>> kyubey = Pet('Kyubey', 'Incubator')
    >>> kyubey.talk()
    Kyubey
    >>> kyubey.eat('Grief Seed')
    Kyubey ate a Grief Seed!
    """
    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner
    
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    
    def talk(self):
        print(self.name)

    def to_str(self):
        return "({}, {})".format(self.name, self.owner)

    def pp(self):
        pretty_print(self)




class Cat(Pet):
    """A cat.

    >>> vanilla = Cat('Vanilla', 'Minazuki Kashou')
    >>> isinstance(vanilla, Pet) # check if vanilla is an instance of Pet.
    True
    >>> vanilla.talk()
    Vanilla says meow!
    >>> vanilla.eat('fish')
    Vanilla ate a fish!
    >>> vanilla.lose_life()
    >>> vanilla.lives
    8
    >>> vanilla.is_alive
    True
    >>> for i in range(8):
    ...     vanilla.lose_life()
    >>> vanilla.lives
    0
    >>> vanilla.is_alive
    False
    >>> vanilla.lose_life()
    Vanilla has no more lives to lose.
    """
    def __init__(self, name, owner, lives=9):
        self.lives = lives
        super().__init__(name, owner)
        self.is_alive = True
        
    def talk(self):
        """ Print out a cat's greeting.
        """
        print(str(self.name)+" says meow!")

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
        becomes False. If this is called after lives has reached zero, print out
        that the cat has no more lives to lose.
        """
        if self.is_alive:
            self.lives-=1
            if self.lives<=0:
                self.is_alive = False
        else:
            print(str(self.name)+" has no more lives to lose.")
        

    def to_str(self):
        """Returns a string representation of the Pet."""
        return "({}, {}, {})".format(self.name, self.owner, self.lives)
    
    def pp(self):
        pretty_print(self)
    



class NoisyCat(Cat): # Dose this line need to change?
    """A Cat that repeats things twice.

    >>> chocola = NoisyCat('Chocola', 'Minazuki Kashou')
    >>> isinstance(chocola, Cat) # check if chocola is an instance of Cat.
    True
    >>> chocola.talk()
    Chocola says meow!
    Chocola says meow!
    """
    
    def talk(self):
        """Talks twice as much as a regular cat.
        """
        super().talk()
        super().talk()
        

    def pp(self):
        pretty_print(self)


class Colors:
    HEADER     = '\033[95m'
    OKBLUE     = '\033[34m'
    OKCYAN     = '\033[35m'
    WARNING    = '\033[93m'
    FAIL       = '\033[91m'
    ENDC       = '\033[0m'
    BOLD       = '\033[1m'
    UNDERLINE  = '\033[4m'


def pretty_print(obj):
    """Pretty prints the object using the Colors class.
    >>> kyubey = Pet('Kyubey', 'Incubator')
    >>> pretty_print(kyubey)
    \033[34mPet\033[0m\033[35m(Kyubey, Incubator)\033[0m
    """
    class_name = type(obj).__name__
    object_str = obj.to_str()
    print(Colors.OKBLUE + class_name + Colors.ENDC + Colors.OKCYAN + object_str + Colors.ENDC)


class Time:
    """ A class that can store and display the date.
    >>> time = Time(2024, 11, 20)
    >>> print(time.to_str())
    24.11.20
    >>> time.setyear(2023)
    >>> time.setmonth(2)
    >>> time.setday(5)
    >>> time.setformat("dd-mm-yy")
    >>> time.to_str()
    '05-02-23'
    >>> time.setformat("yy/mm/dd")
    >>> time.to_str()
    '23/02/05'
    >>> time.setyear(-1)
    Parameter Error!
    >>> time.to_str()
    '23/02/05'
    """
    def __init__(self, year, month, day):
        """Initialize a Time object."""
        """Initialize a Time object."""
        if isinstance(year, int) and year > 0:
            self.year = year
        else:
            print("Parameter Error!")
            self.year = None
        
        if isinstance(month, int) and 1 <= month <= 12:
            self.month = month
        else:
            print("Parameter Error!")
            self.month = None
        
        if isinstance(day, int) and 1 <= day <= 31:
            self.day = day
        else:
            print("Parameter Error!")
            self.day = None
        
        self.format = "yy.mm.dd" 

    def setyear(self, year):
        """Set the year of the Time object."""
        if isinstance(year, int) and year > 0:
            self.year = year
        else:
            print("Parameter Error!")

    def setmonth(self, month):
        """Set the month of the Time object."""
        if isinstance(month, int) and 1 <= month <= 12:
            self.month = month
        else:
            print("Parameter Error!")

    def setday(self, day):
        """Set the day of the Time object."""
        if isinstance(day, int) and 1 <= day <= 31:
            self.day = day
        else:
            print("Parameter Error!")

    def setformat(self, format):
        """Set the format of the Time object."""
        self.format = format

    def to_str(self):
        """Return the formatted date."""
        if self.year:
            year_str = str(self.year)[-2:].zfill(2) 
        else :
            year_str = "00"
        
        if self.month:
            month_str = str(self.month).zfill(2)
        else :
            month_str = "00"
        
        if self.day:
            day_str = str(self.day).zfill(2)
        else :
            day_str = "00"
        result = self.format.replace("yy", year_str).replace("mm", month_str).replace("dd", day_str)
        return result

