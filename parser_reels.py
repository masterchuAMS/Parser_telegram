from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel

all_messages = []
offset_id = 0
limit = 100
total_messages = 0
total_count_limit = 0

while True:
    history = client(GetHistoryRequest(
        peer = target_group,
        offset_id = offset_id,
        offset_date=None,
        add_offset=0,
        limit=limit

    ))