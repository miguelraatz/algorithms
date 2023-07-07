import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    message = "testing"
    assert encrypt_message(message, 4) == "gni_tset"
    assert encrypt_message(message, 2) == "gnits_et"
    assert encrypt_message(message, -2) == "gnitset"

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 2)

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("testing", 5.523)
