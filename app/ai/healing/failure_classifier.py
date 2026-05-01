class FailureClassifier:

    def classify(self, error: str, output: str):

        error = (error or "").lower()

        if "docker" in error or "build" in error:
            return "BUILD_FAILURE"

        if "timeout" in error:
            return "TIMEOUT"

        if "syntax" in error or "indentation" in error:
            return "CODE_SYNTAX_ERROR"

        if "missing" in error or "undefined" in error:
            return "DEPENDENCY_ERROR"

        if "empty" in output:
            return "EMPTY_OUTPUT"

        return "UNKNOWN_FAILURE"