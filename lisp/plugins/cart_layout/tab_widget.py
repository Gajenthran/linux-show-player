# -*- coding: utf-8 -*-
#
# This file is part of Linux Show Player
#
# Copyright 2012-2018 Francesco Ceruti <ceppofrancy@gmail.com>
#
# Linux Show Player is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Linux Show Player is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Linux Show Player.  If not, see <http://www.gnu.org/licenses/>.

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTabWidget


class CartTabWidget(QTabWidget):
    DRAG_MAGIC = 'LiSP_Drag&Drop'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tabBar().setObjectName('CartTabBar')
        self.setFocusPolicy(Qt.StrongFocus)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().text() == CartTabWidget.DRAG_MAGIC:
            event.accept()

    def dragMoveEvent(self, event):
        if self.tabBar().contentsRect().contains(event.pos()):
            self.setCurrentIndex(self.tabBar().tabAt(event.pos()))
            event.accept()

    def dropEvent(self, event):
        event.ignore()

    def pages(self):
        for index in range(self.count()):
            yield self.widget(index)
