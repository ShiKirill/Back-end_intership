import random
import time

from opcua import ua, Server


def get_random_value():
    return random.random() * 20 - 10


if __name__ == "__main__":
    server = Server()
    server.set_endpoint("opc.tcp://127.0.0.1:587")
    idx = server.register_namespace("http://examples.freeopcua.github.io")

    server.load_certificate("certificate-example.der")
    server.load_private_key("private-key-example.pem")

    objects = server.get_objects_node()

    myobj = objects.add_object(idx, "MyObject")
    variables = []

    for i in range(10):
        new_variable = myobj.add_variable(idx, f"var_{i}", get_random_value())
        variables.append(new_variable)

    server.start()
    try:
        while True:
            time.sleep(3)
            for i in range(10):
                new_value = get_random_value()
                variables[i].set_value(new_value)
    finally:
        server.stop()
