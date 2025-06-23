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
        self._statoScelto = None

    def fillYear(self):
        anni = self._model.getAnni()
        for anno in anni:
            self._view.ddyear.options.append(ft.dropdown.Option(key = anno, data = anno, on_click=self._sceltaAnno))
        self._view.update_page()

    def fillStati(self,e):
        self._view.ddstate.options.clear()
        stati = self._model.getStati(self._annoScelto)
        for stato in stati:
            self._view.ddstate.options.append(ft.dropdown.Option(key = str(stato), data = stato, on_click=self._sceltaStato))
        self._view.update_page()

    def handle_graph(self, e):
        self._model.buildGraph(self._annoScelto, self._statoScelto.id)
        n, a = self._model.getGraphDetails()
        self._view.txt_result1.clean()
        self._view.txt_result1.controls.append(ft.Text(f"Numero di nodi: {n}"))
        self._view.txt_result1.controls.append(ft.Text(f"Numero di archi: {a}"))
        self._view.update_page()


    def handle_path(self, e):
        pass

    def _sceltaAnno(self, e):
        self._annoScelto = e.control.data
        print(f"selezionato {self._annoScelto}")

    def _sceltaStato(self, e):
        self._statoScelto = e.control.data
        print(f"selezionato {self._statoScelto}")

