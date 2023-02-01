from vk_api.keyboard import VkKeyboard, VkKeyboardColor

# Клавиатура Главного меню
kb_main_menu = VkKeyboard(one_time=False)
kb_main_menu.add_button('Найти людей', color=VkKeyboardColor.SECONDARY)
kb_main_menu.add_line()
kb_main_menu.add_button('Просмотр избранных', color=VkKeyboardColor.POSITIVE)
kb_main_menu.add_line()
kb_main_menu.add_button('Выход', color=VkKeyboardColor.NEGATIVE)

# Клавиатура Просмотр профиля
kb_profile = VkKeyboard()
kb_profile.add_button('Предыдущий', color=VkKeyboardColor.SECONDARY)
kb_profile.add_button('Следующий', color=VkKeyboardColor.SECONDARY)
kb_profile.add_line()
kb_profile.add_button('Добавить в избранные', color=VkKeyboardColor.POSITIVE)
kb_profile.add_line()
kb_profile.add_button('Выход в главное меню', color=VkKeyboardColor.NEGATIVE)

