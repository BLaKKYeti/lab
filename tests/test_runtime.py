def test_runtime_import():
    from kernel.runtime import Runtime

    assert Runtime is not None
