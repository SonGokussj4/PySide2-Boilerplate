from PySide2.QtCore import QTranslator, QLocale
from PySide2.QtWidgets import QApplication

from ..helpers.logging import setup_logger

logger = setup_logger(__name__)

lang = {
    "cs_CZ": [
        "Čeština",
        "Czech"
    ],
    "en_US": [
        "Angličtina",
        "English"
    ]
}
# key = [key for key, value in lang.items() if "Czech" in value][0]


def get_language_code(lang_text: str) -> str:
    """Get language-code from language name.

    Example:
        - get_language_code('Czech') -> 'cs_CZ'
    """
    if lang_text in {"Czech", "Čeština"}:
        return "cs_CZ"

    elif lang_text in {"English", "Angličtina"}:
        return "en_US"

    logger.warning("Fallback to Czech Language")
    return "cs_CZ"


def get_language_from_code(lang_code: str) -> str:
    """Get language name from language-code.

    Example:
        - get_language_from_code('cs_CZ') -> 'Czech'
    """
    if lang_code == "cs_CZ":
        return "Czech"

    elif lang_code == "en_US":
        return "English"

    logger.warning("Fallback to Czech Language")
    return "Czech"


def load_translations(app: QApplication = None, translator: QTranslator = None, code: str = QLocale.system().name()) -> QTranslator:
    """Load translations by language-code."""
    if not app:
        app = QApplication.instance()

    if not translator:
        translator = QTranslator()

    translator.load(f':/translations/{code}.qm')
    app.installTranslator(translator)

    return translator
