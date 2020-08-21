import main
def test_AlwaysPasses():
    assert(1==1)

def test_Pinging_Loopback_Succeeds():
    IP = "127.0.0.1"
    result = main.pingTheHost(IP)
    assert(result=="Success")

def test_Pinging_Unused_IP_Fails():
    IP = "198.51.100.1"
    result = main.pingTheHost(IP)
    assert(result=="Failure")
    