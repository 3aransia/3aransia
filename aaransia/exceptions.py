class LanguageNotFound(Exception):
    """Exception raised when language alphabet is not found for the language code
    given."""

class SourceLanguageException(Exception):
    """Source language doesn't match the input text"""