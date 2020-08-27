import main


def test_Pinging_Loopback_Succeeds():
    IP = "127.0.0.1"
    result = main.ping_the_host(IP)
    assert(result == "Success")


def test_Pinging_Unused_IP_Fails():
    IP = "198.51.100.1"
    result = main.ping_the_host(IP)
    assert(result == "Failure")
