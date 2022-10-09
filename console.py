from curses import REPORT_MOUSE_POSITION
import pdb
from models.desk import Desk
from models.djequip import Djequip
from models.manufacture import Manufacture
from models.mic import Mic

import repositories.desk_repository as desk_repository
import repositories.djequip_repository as djequip_repository
import repositories.manufacture_repository as manufacture_repository
import repositories.mic_repository as mic_repository

desk_repository.delete_all()
djequip_repository.delete_all()
manufacture_repository.delete_all()
mic_repository.delete_all()