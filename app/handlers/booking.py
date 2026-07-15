from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from app.keyboards.booking_menu_keybords import zone_kb, pack_kb
from app.database.reposytory import create_user, get_user, create_bk_user, get_bk_user
from app.states.booking_states import BookingForm
from app.utils.content import ENTER_NAME, ENTER_ZONE, ENTER_PACK, ENTER_DATE


bk_router = Router(name = "bk_router")

@bk_router.callback_query(F.data == "application")
async def wait_name(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(ENTER_NAME)
    await state.set_state(BookingForm.wait_name)
    await callback.answer()

@bk_router.callback_query(BookingForm.wait_name)
async def wait_zone(callback:CallbackQuery, state: FSMContext):

