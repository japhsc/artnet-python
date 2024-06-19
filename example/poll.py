from threading import Thread
from typing import Any

from artnet import ArtNet, OpCode


def poll_request(op_code: OpCode, ip: str, port: int, reply: dict[str, Any]) -> None:
    print(f"Received {op_code.name} (request) from {ip}:{port}")

    for k, v in reply.items():
        print(f"\t{k} = {v}")


def poll_reply(op_code: OpCode, ip: str, port: int, reply: dict[str, Any]) -> None:
    print(f"Received {op_code.name} from {ip}:{port}")

    for k, v in reply.items():
        print(f"\t{k} = {v}")


def main():
    artnet = ArtNet()

    artnet.subscribe(OpCode.ArtPoll, poll_request)
    artnet.subscribe(OpCode.ArtPollReply, poll_reply)

    x = Thread(target=artnet.listen, kwargs=dict(timeout=3.0))
    x.start()

    artnet.send_poll()

    x.join()


if __name__ == "__main__":
    main()
