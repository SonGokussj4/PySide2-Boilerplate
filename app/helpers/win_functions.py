from PySide2.QtCore import QSize, QPoint, QSettings
from PySide2.QtWidgets import QDesktopWidget
from app.helpers import constants


def setSizeAndPosition(window) -> None:
    """Set window size and position."""
    # Get window size and position from settings
    settings = QSettings(constants.APP_NAME, "General")

    win_name = window.objectName()
    _size = QSize(settings.value(f"{win_name}/size", QSize(*constants.default_main_window_size)))
    _pos = QPoint(settings.value(f"{win_name}/pos", getCenterPoint(window)))

    # Set window size and position
    size = _size if _size else QSize(*constants.default_main_window_size)
    pos = _pos if _pos else getCenterPoint(window)

    window.setGeometry(*pos.toTuple(), *size.toTuple())


def getCenterPoint(window) -> QPoint:
    """Get window center point."""
    qr = window.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    return qr.topLeft()
