import time

import pystache


class Utils:
    @classmethod
    def parse(self, template_path, dict):
        template = "".join(open(template_path).readlines())

        return pystache.render(template, dict)

    @classmethod
    def udid(cls):
        return str(time.time()).replace(".", "")[3:11]
