from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class TodoListSeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()  # Cambia esto por el navegador que estés utilizando
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_index_page(self):
        # Abrir la página de inicio
        self.selenium.get(self.live_server_url)

        # Verificar si el título de la página es correcto
        self.assertIn('Todo List', self.selenium.title)

        # Verificar si se muestra el mensaje de "No tienes listas"
        empty_message = self.selenium.find_element_by_tag_name('h4')
        self.assertEqual(empty_message.text, 'You have no lists!')

        # Verificar si se muestra el botón de "Agregar nueva lista"
        add_button = self.selenium.find_element_by_xpath("//input[@value='Add a new list']")
        self.assertTrue(add_button.is_displayed())

        # Verificar si se muestran las listas (si existen)
        list_items = self.selenium.find_elements_by_css_selector('.list-item')
        if list_items:
            # Si hay listas, verificar que el primer elemento tenga un título válido y sea clickeable
            first_list = list_items[0]
            self.assertTrue(first_list.is_displayed())
            first_list.click()

            # Verificar que nos redirige a la página de la lista correcta
            self.assertIn('/list/', self.selenium.current_url)

