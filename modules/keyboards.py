from vk_api.keyboard import VkKeyboard, VkKeyboardColor

# Клавиатура Главного меню
kb_main_menu = VkKeyboard(one_time=False)
kb_main_menu.add_button('Найти людей', color=VkKeyboardColor.SECONDARY)
kb_main_menu.add_line()
kb_main_menu.add_button('Просмотр избранных', color=VkKeyboardColor.POSITIVE)
kb_main_menu.add_line()
kb_main_menu.add_button('Выход', color=VkKeyboardColor.NEGATIVE)