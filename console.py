from curses import REPORT_MOUSE_POSITION
import pdb
from models.product import Product
from models.manufacture import Manufacture
from models.type import Type

import repositories.manufacture_repository as manufacture_repository
import repositories.product_repository as product_repository
import repositories.type_repository as type_repositpory


manufacture_repository.delete_all()
product_repository.delete_all()
type_repositpory.delete_all()


# SEED DATA

type1 = Type('Microphone')
type_repositpory.save(type1)
type2 = Type('Live Console')
type_repositpory.save(type2)
type3 = Type('DJ Equipment')
type_repositpory.save(type3)

manufacture1 = Manufacture('Shure')
manufacture_repository.save(manufacture1)
manufacture2 = Manufacture('Allen & Heath')
manufacture_repository.save(manufacture2)
manufacture3 = Manufacture('Pioneer')
manufacture_repository.save(manufacture3)

product1 = Product('SM58', 'Standard vocal microphone', 5, 69.99, 125.00, manufacture1, type1)
product_repository.save(product1)

product2 = Product('SQ7', 'Newest digit mixer in the budget range', 2, 1700, 2500, manufacture2, type2)
product_repository.save(product2)

product3 = Product('CDJ2000', 'Classic CDJ player for anyones rider', 4, 1400, 2200, manufacture3, type3)
product_repository.save(product3)

pdb.set_trace()