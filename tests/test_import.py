def test_import_speech_recognition():
    import importlib
    mod = importlib.import_module("speech_recognition")
    assert mod is not None
