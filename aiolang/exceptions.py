class TranslationError(Exception):
    """Custom exception for translation errors"""

    def __init__(self, message: str, solution: str = None):
        self.message = message
        self.solution = solution
        super().__init__(self.message)

    def __str__(self):
        if self.solution:
            return f"{self.message} (Suggested solution: {self.solution})"
        return self.message