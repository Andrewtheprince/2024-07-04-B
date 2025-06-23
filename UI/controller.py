import flet as ft
from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._annoScelto = None

    def fillYear(self):
        anni = self._model.getAnni()
        for anno in anni:
            self._view.ddyear.options.append(ft.dropdown.Option(key = anno, data = anno, on_click=self._sceltaAnno))
        self._view.update_page()

    def handle_graph(self, e):
        pass

    def handle_path(self, e):
        pass

    def _sceltaAnno(self, e):
        self._annoscelto = e.control.data

