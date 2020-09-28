import io
import json

from hop.io import Deserializer
from hop.plugins import snews


def test_plugin():
    # check that message types are registered
    assert 'SNEWSOBSERVATION' in Deserializer.__members__
    assert 'SNEWSHEARTBEAT' in Deserializer.__members__
    assert 'SNEWSALERT' in Deserializer.__members__


def test_load():
    message_id = "random-message-id"
    serialized = json.dumps({"message_id": message_id})

    # check that load functionality works correctly
    message = snews.SNEWSBase.load(serialized)
    assert message.message_id == message_id

    with io.StringIO(serialized) as f:
        message = snews.SNEWSBase.load(f)
    assert message.message_id == message_id
