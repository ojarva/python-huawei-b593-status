import sys
import xmltodict
import httplib2

STAT = {
    "WIFI": {
        2: "on",
        3: "trans",
        4: "off",
    },
    "SIM": {
        14: "no_sim",
        15: "normal",
        16: "pin_locked",
        17: "error",
    },
    "SIG": {
        18: "off",
        19: "1",
        20: "2",
        21: "3",
        22: "4",
        23: "5",
    },
    "Connect": {
        24: "no_connect",
        25: "connecting",
        26: "connected",
    },
    "Mode": {
        27: "off",
        28: "2g",
        29: "3g",
        30: "4g",
        59: "sim_disabled",
        60: "2g",
        61: "3g",
        62: "4g",
    },
    "Roam": {
        31: "home",
        32: "roaming",
        33: "forbidden",
    },
}


class HuaweiStatus:
    def __init__(self, url="https://elisa.home/index/getStatusByAjax.cgi?rid=134"):
        self.url = url

    def read(self):
        h = httplib2.Http(disable_ssl_certificate_validation=True)
        (resp_headers, content) = h.request(self.url, "POST")
        if resp_headers["status"] != "200":
            raise IOError("Invalid status code:", resp_headers["status"])
        obj = xmltodict.parse(content)
        ret = {}
        for k in STAT:
            ret[k] = STAT[k][int(obj["Status"][k])]
        return ret


def main():
    huawei = HuaweiStatus()
    print huawei.read()
    return 0

if __name__ == '__main__':
    sys.exit(main())
