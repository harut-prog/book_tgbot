from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON
from services.file_handling import book

# Функция, генерирующая клавиатуру для страницы книги
def pagination_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Добавляем в билдер ряд с кнопками
    kb_builder.row(*[InlineKeyboardButton(
        text=LEXICON[button] if button in LEXICON else button,
        callback_data=button) for button in buttons]
    )
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()

# Функция-обертка для клавиатуры, чтобы отображать кнопки перехода в соответствии с текущей страницей
def create_pagination_keyboard(page=1) -> InlineKeyboardMarkup:
    middle_button = f'{page}/{len(book)}'
    if page == 1:
        return pagination_keyboard(middle_button, 'forward')
    elif 1 < page < len(book):
        return pagination_keyboard('backward', middle_button, 'forward')
    else:
        return pagination_keyboard('backward', middle_button)