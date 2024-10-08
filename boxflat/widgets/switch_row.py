import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
from .row import BoxflatRow

class BoxflatSwitchRow(BoxflatRow):
    def __init__(self, title: str, subtitle=""):
        super().__init__(title, subtitle)

        switch = Gtk.Switch()
        switch.add_css_class("switch")
        switch.connect('notify::active', lambda switch, whatever: self._notify())
        switch.set_valign(Gtk.Align.CENTER)
        self._reverse = False
        self._switch = switch
        self._set_widget(switch)
        self.set_activatable_widget(switch)


    def get_value(self) -> int:
        val = self._switch.get_active()
        if self._reverse:
            val = not val

        return round(eval("int(val)" + self._expression))


    def reverse_values(self) -> None:
        self._reverse = True


    def _set_value(self, value: int) -> None:
        if value < 0:
            return

        val = round(eval("value"+self._reverse_expression))
        if val < 0:
            val = 0
        if self._reverse:
            val = not bool(val)
        self._switch.set_active(bool(val))
