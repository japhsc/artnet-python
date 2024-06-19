from threading import Thread
from typing import Any

from artnet import ArtNet, OpCode


def receive(op_code: OpCode, ip: str, port: int, reply: Any) -> None:
    print(f"Received {op_code.name} from {ip}:{port}")

    for k, v in reply.items():
        print(f"\t{k} = {v}")


def main():
    artnet = ArtNet()

    artnet.subscribe_all(receive)

    x = Thread(target=artnet.listen, kwargs=dict(timeout=None))
    x.start()

    artnet.send_dmx(1, 0, bytearray([0] * 512))

    x.join()


if __name__ == "__main__":
    main()
