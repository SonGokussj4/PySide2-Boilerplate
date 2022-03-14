from PySide2.QtCore import QTranslator
from ..helpers.logging import setup_logger

logger = setup_logger(__name__)


def get_language_code(lang_text):
    if lang_text in {"Czech", "Čeština"}:
        return "cs_CZ"

    elif lang_text in {"English", "Angličtina"}:
        return "en_US"

    logger.warning("Fallback to Czech Language")
    return "cs_CZ"


def load_translations(app, code):
    """Load translations by code."""
    trans = QTranslator()
    trans.load(f':/translations/{code}.qm')
    app.installTranslator(trans)
    return trans
