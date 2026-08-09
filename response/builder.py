from execution.result import ExecutionResult


class ResponseBuilder:
    def build(self, results):
        if not results:
            return "No result."

        responses = []

        for result in results:
            if not isinstance(result, ExecutionResult):
                continue

            if not result.success:
                responses.append(
                    f"{result.plugin}.{result.action} failed: {result.output}."
                )
                continue

            responses.append(self._format_success(result))

        if not responses:
            return "No result."

        return "\n".join(responses)

    def _format_success(self, result):
        if result.plugin == "time":
            if result.action == "current_time":
                return f"The current time is {result.output}."

            if result.action == "current_date":
                return f"Today's date is {result.output}."

        if result.plugin == "filesystem":
            if result.action == "list_pdfs":
                if isinstance(result.output, list):
                    count = len(result.output)

                    if count == 0:
                        return "I found no PDF files."

                    if count == 1:
                        return "I found 1 PDF file."

                    return f"I found {count} PDF file(s)."

        return str(result.output)
