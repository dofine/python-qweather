class ApiError(Exception):
    """Raised when QWeather API request ended in error."""

    def __init__(self, status: str):
        """Initialize."""
        super().__init__(status)
        self.status = status


class InvalidApiKeyError(Exception):
    """Raised when API Key format is invalid."""

    def __init__(self, status: str):
        """Initialize."""
        super().__init__(status)
        self.status = status


class InvalidCoordinatesError(Exception):
    """Raised when coordinates are invalid."""

    def __init__(self, status: str):
        """Initialize."""
        super().__init__(status)
        self.status = status


class RequestsExceededError(Exception):
    """Raised when allowed number of requests has been exceeded."""

    def __init__(self, status: str):
        """Initialize."""
        super().__init__(status)
        self.status = status