def test_phrase_length():
    phrase = input("Set a phrase: ")
    max_length = 15
    assert len(phrase) <= max_length, f"Input phrase has more then {max_length} letters!"
    print(f"Phrase length: {len(phrase)}")


class Example10:
    pass