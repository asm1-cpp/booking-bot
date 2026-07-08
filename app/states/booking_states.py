from aiogram.fsm.state import State, StatesGroup

class BookingForm(StatesGroup):
    name = State()
    phone = State()
    date = State()
    confirm = State()
    waiting_for_admin = State()
