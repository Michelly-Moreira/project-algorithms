from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    pass
    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message(message='message', key='message')

    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(message=10, key=2)

    assert encrypt_message('message', 8) == 'egassem'

    assert encrypt_message('message', 2) == 'egass_em'

    assert encrypt_message('message', 3) == 'sem_egas'
