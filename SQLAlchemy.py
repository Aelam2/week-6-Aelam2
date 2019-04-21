from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import datetime

Base = declarative_base()

#Simple Order class for Pizza ordering system
class PizzaOrder(Base):

    #Online accounts would be associated with a Customer Number
    def __init__(self, customerNumber, orderTotal, dateOrdered):
        self.customerNumber = customerNumber
        self.orderTotal = orderTotal
        self.dateOrdered = dateOrdered

    def __str__(self):
        return 'Customer Number: {0}, Order Total: {1}, Ordered on: {2}'.format(self.customerNumber, self.orderTotal, self.dateOrdered)

    __tablename__ = 'orders'

    orderId = Column(Integer, primary_key = True)
    customerNumber = Column(Integer)
    orderTotal = Column(Integer)
    dateOrdered = Column(DateTime, default=datetime.datetime.utcnow)


def main():
    engine = create_engine('sqlite:///:memory:', echo=False)

    #Create Test Orders
    orderOne = PizzaOrder('12345', 16.32, datetime.datetime.now() )
    orderTwo = PizzaOrder('3215', 12.23, datetime.datetime.now())
    orderThree = PizzaOrder('73143', 32.11, datetime.datetime.now())

    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    #Add orders to database
    session.add(orderOne)
    session.add(orderTwo)
    session.add(orderThree)
    session.commit()

    #Retrieve Orders
    orders = session.query(PizzaOrder).all()

    for order in orders:
        print('Order Number', order.orderId, 'Details=', order)

    #Close connection
    session.close()

main()