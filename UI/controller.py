import flet as ft
from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        pass

    def handle_path(self, e):
        pass

    def fill_ddyear(self):
        years = self._model.get_years()
        self._view.ddyear.options.clear()
        for y in years:
            self._view.ddyear.options.append(ft.dropdown.Option(f"{y}"))

    def fill_ddstate(self, e):
        anno = int(self._view.ddyear.value)
        self._view.ddstate.options.clear()
        self._view.ddstate.value = None
        shapes = self._model.get_states_year(anno)
        for s in shapes:
            self._view.ddstate.options.append(ft.dropdown.Option(key=s.id,text=s.name))
        self._view.update_page()