from execution.result import ExecutionResult
from response.builder import ResponseBuilder


def test_response_builder_formats_time_result():
    builder = ResponseBuilder()

    results = [
        ExecutionResult(
            plugin="time",
            action="current_time",
            success=True,
            output="12:34:56",
        )
    ]

    response = builder.build(results)

    assert response == "The current time is 12:34:56."


def test_response_builder_formats_date_result():
    builder = ResponseBuilder()

    results = [
        ExecutionResult(
            plugin="time",
            action="current_date",
            success=True,
            output="2026-08-08",
        )
    ]

    response = builder.build(results)

    assert response == "Today's date is 2026-08-08."


def test_response_builder_formats_pdf_result():
    builder = ResponseBuilder()

    results = [
        ExecutionResult(
            plugin="filesystem",
            action="list_pdfs",
            success=True,
            output=[
                "C:\\Users\\A.pdf",
                "C:\\Users\\B.pdf",
                "C:\\Users\\C.pdf",
            ],
        )
    ]

    response = builder.build(results)

    assert response == "I found 3 PDF file(s)."


def test_response_builder_handles_empty_pdf_result():
    builder = ResponseBuilder()

    results = [
        ExecutionResult(
            plugin="filesystem",
            action="list_pdfs",
            success=True,
            output=[],
        )
    ]

    response = builder.build(results)

    assert response == "I found no PDF files."


def test_response_builder_handles_failure():
    builder = ResponseBuilder()

    results = [
        ExecutionResult(
            plugin="time",
            action="current_time",
            success=False,
            output="Something went wrong",
        )
    ]

    response = builder.build(results)

    assert response == "time.current_time failed: Something went wrong."


def test_response_builder_handles_multiple_results():
    builder = ResponseBuilder()

    results = [
        ExecutionResult(
            plugin="filesystem",
            action="list_pdfs",
            success=True,
            output=[
                "C:\\Users\\A.pdf",
                "C:\\Users\\B.pdf",
            ],
        ),
        ExecutionResult(
            plugin="time",
            action="current_time",
            success=True,
            output="12:34:56",
        ),
    ]

    response = builder.build(results)

    assert response == ("I found 2 PDF file(s).\nThe current time is 12:34:56.")
